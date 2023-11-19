#!/usr/bin/python3
"""module to define state relationships"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """class to create state relationships"""
    __tablename__ = 'states'

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state', cascade='all, delete-orphan')
