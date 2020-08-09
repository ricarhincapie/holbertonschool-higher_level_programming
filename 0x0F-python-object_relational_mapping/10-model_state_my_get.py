#!/usr/bin/python3
"""Shows all objects from tables states"""
import sys
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    user_query = sys.argv[4]

    result = session.query(State).filter(State.name == user_query).first()
    # The main result here was bad with .all(). Worked with .first()
    if result is None:
        print("Not found")
    else:
        print(result.id)

    session.close()
