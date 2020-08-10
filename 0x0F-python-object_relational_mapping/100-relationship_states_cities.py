#!/usr/bin/python3
"""Shows all objects from tables states"""
import sys
from sqlalchemy import create_engine
from relationship_state import State
from relationship_city import City, Base
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name='California')
    new_city = City(name="San Francisco", state=new_state)

    session.add(new_city)
    session.commit()
    session.close()
