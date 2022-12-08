#!/usr/bin/python3
# A Python file similar to model_state.py named model_city.py
# that contains the class definition of a City
"""Prints all City objects from the database hbtn_0e_14_usa."""

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
from sys import argv


if __name__ == "__main__":
    # Create engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    # Create session
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    # Query
    cities = session.query(City, State).filter(City.state_id == State.id).all()
    for city, state in cities:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    # Close session
    session.close()