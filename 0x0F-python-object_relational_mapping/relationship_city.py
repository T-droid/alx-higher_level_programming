#!/usr/bin/python3
"""module to define City relationships"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, Column, ForeignKey, String
from relationship_state import Base

class City(Base):
    """class to create city relationships"""
    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
