# -*- coding: utf-8 -*-
from sqlalchemy.orm import Session

from . import models, schemas
from fastapi import HTTPException


#to calculate the distances of address with respect to base location
import geopy.distance

#Here is our the base location coordinates
cord2 = (12.910592, 77.630669)

#check if map_latitude and map_longitude already exist
def get_address_by_coordinates(db: Session,map_latitude:float,map_longitude:float):
    return db.query(models.Address).filter(models.Address.map_latitude == map_latitude,models.Address.map_longitude == map_longitude).first()

#to get only those addresses that are in given distance to base location.
# the default value of distance is set to 500 KM if distance is None
def get_address_by_distance(db: Session,distance: int | None= None):
    address = db.query(models.Address).all()
    if distance is None:
        distance = 500 
    li=[]
    for a in address:
        cord1= (a.map_latitude,a.map_longitude)
        if geopy.distance.geodesic(cord1, cord2).km < distance:
            li.append(a.id)      
    return db.query(models.Address).filter(models.Address.id.in_(li)).all()

#a get method to get all the distances ---  Not needed
def get_address(db: Session):
    return db.query(models.Address).all()

#to create a new address with latitute and longitude 
def create_address(db: Session, address: schemas.Addresscreate):
    db_user = models.Address(**address.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

#to update the address with new latitute and longitude 
def update_address(id:int,db: Session, address: schemas.Addressupdate):
    db_address = db.query(models.Address).filter(models.Address.id==id).first()
    if not db_address:
        raise HTTPException(status_code=404, detail="address not found")
    for key, value in address.dict().items():
        if value is not None:
            setattr(db_address, key, value)

    db.commit()
    db.refresh(db_address)

    return db_address

#to delete the address from the id provided
def delete_address(id:int,db: Session):
    db_address = db.query(models.Address).filter(models.Address.id==id).first()
    if not db_address:
        raise HTTPException(status_code=404, detail="address not found")
    db.delete(db_address)
    db.commit()

    return db_address
