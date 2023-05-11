# -*- coding: utf-8 -*-

from sqlalchemy import Boolean, Column, ForeignKey, Integer, Float

from .database import Base

#defining the address Table in data base
class Address(Base):
    __tablename__ = "adress"

    id = Column(Integer, primary_key=True, index=True)
    map_latitude =  Column(Float)
    map_longitude=Column(Float)
    