#!/usr/bin/python3
"""Start link class to table in database 
"""
import sys
from model_state import Base, State # Imports from my schema document the declarative_base() instance and the class schema

from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    # Here connects to the data base via create_engine
    Base.metadata.create_all(engine)
    # Here metadata, which collects data about baeses an tables, is flushed into the real database with the create_all method
    # and the specific engine (db) is specified for it. 