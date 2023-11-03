# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#URL to connect to our DB
SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db" 

#Create a DB engine too connect to SQLlite DB
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

#session will be used every time we interact with DB
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#creating a declarative_base object that will be used our Models
Base = declarative_base()