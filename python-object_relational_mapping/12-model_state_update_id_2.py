#!/usr/bin/python3
# A script that changes the name of a State object
# from the database hbtn_0e_6_usa

"""Changes the name of a State object from the database."""

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
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
    state = session.query(State).filter(State.id == 2).first()
    state.name = "New Mexico"
    session.commit()
    # Close session
    session.close()