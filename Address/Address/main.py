# -*- coding: utf-8 -*-

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import models, schemas
from .database import SessionLocal, engine

from .crud import AdressBook #get_address_by_coordinates,get_address_by_distance,get_address,create_address,update_address,delete_address,cord2



import logging
from fastapi.logger import logger

app = FastAPI()

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




# Everytime we interact with DB with our API an DB session is opened and is closed
# This is used as an Dependency in our end points
async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



ab=AdressBook()
#API endpoint to create a new adress it depends on get_db method
@app.post("/address_add/", response_model=schemas.Address)
async def create_address1(address: schemas.Addresscreate, db: Session = Depends(get_db)):
    db_address = ab.get_address_by_coordinates(db,map_latitude=address.map_latitude, map_longitude=address.map_longitude)
    if db_address:
        logger.debug(f'/address_add/ - data already registered for address book request for latitude: {address.map_latitude} longitude: {address.map_longitude}' )
        raise HTTPException(status_code=400, detail="address already registered")
    logger.info(f'/address_add/ - Processing address book request for latitude: {address.map_latitude} longitude: {address.map_longitude}')
    return ab.create_address(db=db, address=address)

#end point to get only those address within a distance, if no distance is provided or None then defualt distance is 500 KM
@app.get("/address_get/", response_model=list[schemas.Address])
async def read_address(distance: int | None = None,db: Session = Depends(get_db)):
    if distance:
        logger.info(f'/address_get/ - Processing address request for distance: {distance} KM')
    else :
        logger.info('/address_get/ - Processing address request for default distance: 500 KM')
    address = ab.get_address_by_distance(db,distance,logger)
    return address

#end point to get all address from DB depends on get_db method
@app.get("/address_all/", response_model=list[schemas.Address])
async def read_all_address(db: Session = Depends(get_db)):
    logger.info('/address_all/ - Processing all address Request')
    address = ab.get_address(db)
    return address

#end point to Update address for given ID depends on get_db method
@app.patch("/address_update/{id}", response_model=schemas.Address)
async def update_address(id:int,address: schemas.Addressupdate, db: Session = Depends(get_db)):
    address = ab.update_address(id,db,address=address)
    logger.info(f'/address_update/ - Processed update address Request for ID : {id}')
    return address


#end point to delete address for given ID depends on get_db method
@app.delete("/address_delete/{id}")
async def delete_address(id: int, db: Session = Depends(get_db)):
    address = ab.delete_address(id,db)
    logger.info(f'/address_delete/ - Processed delete address Request for ID : {id}')
    return {"message": "Task deleted successfully","data":address}
