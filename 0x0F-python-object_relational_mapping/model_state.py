#!/usr/bin/python3
"""
class definition of a State and an instance Base
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
import sqlalchemy

Base = declarative_base()

class State(Base):
    """Representation of State class"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
