#!/usr/bin/python3
"""
Start link class to table in database
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base, State
from sqlalchemy.orm import relationship


class City(Base):
    """
    Class City that defines a db table
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)
    state = relationship("State")
