#!/usr/bin/python3
"""Defines the schema for the table State
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, backref
from relationship_city import Base, City


class State(Base):
    """State class"""
    __tablename__ = 'states'

    id = Column(Integer,
                primary_key=True,
                nullable=False,
                autoincrement="auto",
                unique=True)
    name = Column(String(128),
                  nullable=False)

    cities = relationship("City", backref="state", cascade="all, delete")
