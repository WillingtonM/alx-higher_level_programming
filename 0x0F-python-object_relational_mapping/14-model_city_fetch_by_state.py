#!/usr/bin/python3
"""
script prints all City objects from database
"""

import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sys import argv
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    db_eng = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],
                                                                    argv[2],
                                                                    argv[3]
                                                                    ))
    Base.metadata.create_all(db_eng)
    Session = sessionmaker(bind=db_eng)
    sess = Session()
    db_rows = sess.query(City, State).filter(City.state_id == State.id)\
                                     .order_by(City.id).all()
    for db_city, db_state in db_rows:
        print("{}: ({}) {}".format(db_state.name, db_city.id, db_city.name))
    sess.close()
