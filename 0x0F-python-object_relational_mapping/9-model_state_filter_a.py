#!/usr/bin/python3
"""
script list State objects that contain letter a from database
"""

import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State
from sys import argv

if __name__ == "__main__":
    db_eng = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],
                                                                    argv[2],
                                                                    argv[3]
                                                                    ))
    Base.metadata.create_all(db_eng)
    Session = sessionmaker(bind=db_eng)
    sess = Session()
    val = '%a%'
    db_states = sess.query(State).filter(State.name.like(val)).order_by(State.id)
    for db_state in db_states:
        print("{}: {}".format(db_state.id, db_state.name))
    sess.close()
