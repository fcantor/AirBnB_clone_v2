#!/usr/bin/python3
"""This is the state class"""
import models
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = 'states'
    name = Column(String(128),
                  nullable=False)
    cities = relationship("City",
                          cascade="all")
    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            ''' Returns list of city instances '''
            results = storage.all(City)
            city_list = []
            for k, v in results.items():
                if v.state_id == self.id:
                    city_list.append(v)
            return city_list
