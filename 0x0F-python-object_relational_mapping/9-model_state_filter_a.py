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

    result = session.query(State).filter(State.name.ilike('%a%')).all()
    # The above query uses ILIKE instead of LIKE because the former
    # is NOT case sensitive

    if result is None:  # Checks wheter the query did not return values
        print("Nothing")
    else:
        for row in result:
            print("{}: {}".format(row.id, row.name))

    session.close()
