#!/usr/bin/python3
"""
script adds State object Louisiana to database
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
    n_state = State(name='Louisiana')
    sess.add(n_state)
    db_states = sess.query(State).filter_by(name='Louisiana').first()
    print(str(db_states.id))
    sess.commit()
    sess.close()
