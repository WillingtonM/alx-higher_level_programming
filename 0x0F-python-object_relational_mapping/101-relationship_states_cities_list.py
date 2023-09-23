#!/usr/bin/python3
"""
script lists State objects & corresponding City objects contained in database
"""

import sqlalchemy
from relationship_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import City
from sys import argv


if __name__ == "__main__":
    db_eng = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(argv[1],
                                                                    argv[2],
                                                                    argv[3]))
    Base.metadata.create_all(db_eng)
    Session = sessionmaker(bind=db_eng)
    sess = Session()
    db_rows = sess.query(State).all()
    for db_state in db_rows:
        print("{}: {}".format(db_city.id, db_state.name))
        for db_city in db_state.cities:
            print("    {}: {}".format(db_city.id, db_city.name))
    sess.close()
