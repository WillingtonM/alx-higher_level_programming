#!/usr/bin/python3
"""
script creates the State California with the City San Francisco from database
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
                                                                    argv[3]
                                                                    ))
    Base.metadata.create_all(db_eng)
    Session = sessionmaker(bind=db_eng)
    sess = Session()
    cali_state = State(name="California")
    cali_state.cities = [City(name="San Francisco")]
    sess.add(cali_state)
    sess.commit()
    sess.close()
