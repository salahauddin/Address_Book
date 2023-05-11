# -*- coding: utf-8 -*-

from pydantic import BaseModel


#defining schemas of our DB tables
class Address(BaseModel):
    id: int
    map_latitude: float 
    map_longitude: float 
    
    class Config:
        orm_mode = True

#to validate that the Latitude and Logitue values are in float
class Addresscreate(BaseModel):
    map_latitude: float 
    map_longitude: float 
    
#Schemas to be used while updating the Address for a particular ID
class Addressupdate(BaseModel):
    map_latitude: float | None=None
    map_longitude: float | None=None
