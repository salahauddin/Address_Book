# -*- coding: utf-8 -*-
from sqlalchemy.orm import Session

from . import models, schemas


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