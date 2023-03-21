#!/usr/bin/python3
""" City Module for HBNB project """
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from models.base_model import BaseModel, Base
from sqlalchemy import ForeignKey


class City(BaseModel):
    """ The City class, contains state id and name
    Attributes:
        state_id: The state id
        name: input name
    """
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
