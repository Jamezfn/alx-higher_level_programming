#!/usr/bin/python3
"""State class definition and SQLAlchemy setup for states table"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class State(Base):
    """State that maps to the states table"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)

    cities = relationship("City", back_populates="state", cascade="all, delete")
