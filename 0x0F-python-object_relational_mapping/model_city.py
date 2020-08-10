#!/usr/bin/python3
"""Defines the schema for the table State
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
# from model_state import Base

Base = declarative_base()


class City(Base):
    """City class Schema"""
    __tablename__ = 'cities'
    id = Column(Integer,
                primary_key=True,
                autoincrement=True,
                nullable=False,
                unique=True)
    name = Column(String(128),
                  nullable=False)

    state_id = Column(Integer,
                      ForeignKey("states.id"),
                      nullable=False)
