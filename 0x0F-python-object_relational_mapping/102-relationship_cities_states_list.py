#!/usr/bin/python3
"""
script lists City objects from database
"""

import sqlalchemy
from sqlalchemy import create_engine
from relationship_state import Base, State
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
    db_rows = sess.query(City).all()
    for db_city in db_rows:
        print("{}: {} -> {}".format(db_city.id, db_city.name, db_city.state.name))
    sess.close()
