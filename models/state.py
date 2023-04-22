#!/usr/bin/python3
''' State Module for HBNB project '''
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from models.city import City
import models
import shlex


class State(BaseModel, Base):
    '''This is the class for State
    Attributes:
        name: input name
    '''
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', cascade='all, delete, delete-orphan',
                          backref='state')

    @property
    def cities(self):
        store = models.storage.all()
        a_list = []
        result = []
        for key in store:
            city = key.replace('.', ' ')
            city = shlex.split(city)
            if (city[0] == 'City'):
                a_list.append(store[key])
        for item in a_list:
            if (item.state_id == self.id):
                result.append(item)
        return (result)
