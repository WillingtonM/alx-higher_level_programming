#!/usr/bin/python3
"""
Defines classes for tables
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base, State
import sqlalchemy


class City(Base):
    """Creates table for cities"""
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))
