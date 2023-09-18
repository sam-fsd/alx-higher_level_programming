#!/usr/bin/python3
"""
City model definition
"""

from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Integer, ForeignKey


Base = declarative_base()


class City(Base):
    """Schema for a city"""
    __tablename__ = 'cities'

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'),
                      nullable=False)
