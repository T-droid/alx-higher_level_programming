#!/usr/bin/python3
"""module to define class City"""


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, Column, ForeignKey, String
Base = declarative_base()

class City(Base):
    """class to define table cities"""
    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
