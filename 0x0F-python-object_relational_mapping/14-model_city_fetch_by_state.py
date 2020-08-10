#!/usr/bin/python3
"""Shows all objects from tables states"""
import sys
from sqlalchemy import create_engine
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(City, State).filter(City.state_id == State.id) \
                                       .order_by(City.id).all()

    for city, state in result:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
