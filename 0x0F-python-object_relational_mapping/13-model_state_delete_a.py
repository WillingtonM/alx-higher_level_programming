#!/usr/bin/python3
"""
script deletes all State objects with name containing letter from database
"""

import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sys import argv
from model_state import Base, State


if __name__ == "__main__":
    db_eng = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],
                                                                    argv[2],
                                                                    argv[3]
                                                                    ))
    Base.metadata.create_all(db_eng)
    Session = sessionmaker(bind=db_eng)
    sess = Session()
    db_states = sess.query(State).filter(State.name.like('%a%'))
    for db_state in db_states:
        sess.delete(db_state)
    sess.commit()
    sess.close()
