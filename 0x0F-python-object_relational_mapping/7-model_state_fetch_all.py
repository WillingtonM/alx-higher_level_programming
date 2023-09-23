#!/usr/bin/python3
"""
script lists State objects from database
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
    for db_state in sess.query(State).order_by(State.id):
        print("{}: {}".format(db_state.id, db_state.name))
    sess.close()
