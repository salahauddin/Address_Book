# -*- coding: utf-8 -*-

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine


import logging
from fastapi.logger import logger


# Create a logger object
logger = logging.getLogger(__name__)

# Set level of logger
logger.setLevel(logging.DEBUG)

# Create a file handler
handler = logging.FileHandler('logfile.log')

# Create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# Add the handler to the logger
logger.addHandler(handler)

#defining meta data for models
models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Everytime we interact with DB with our API an DB session is opened and is closed
# This is used as an Dependency in our end points
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


#API endpoint to create a new adress it depends on get_db method
@app.post("/address/", response_model=schemas.Address)
def create_address(address: schemas.Addresscreate, db: Session = Depends(get_db)):
    db_address = crud.get_address_by_coordinates(db,map_latitude=address.map_latitude, map_longitude=address.map_longitude)
    if db_address:
        logger.debug(f'data already registered for address book request for latitude: {address.map_latitude} longitude: {address.map_longitude}' )
        raise HTTPException(status_code=400, detail="address already registered")
    logger.info(f'Processing address book request for latitude: {address.map_latitude} longitude: {address.map_longitude}')
    return crud.create_address(db=db, address=address)

#end point to get only those address within a distance, if no distance is provided or None then defualt distance is 500 KM
@app.get("/address/", response_model=list[schemas.Address])
def read_address(distance: int | None = None,db: Session = Depends(get_db)):
    if distance:
        logger.info(f'Processing address request for distance: {distance} KM')
    else :
        logger.info('Processing address request for default distance: 500 KM')
    address = crud.get_address_by_distance(db,distance)
    return address

#end point to get all address from DB depends on get_db method
@app.get("/address_all/", response_model=list[schemas.Address])
def read_all_address(db: Session = Depends(get_db)):
    logger.info('Processing all address Request')
    address = crud.get_address(db)
    return address