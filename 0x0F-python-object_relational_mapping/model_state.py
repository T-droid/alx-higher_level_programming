#!/usr/bin/python3
"""module to define class state"""
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """ class to define state"""
    __tablename__ = 'states'

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)
