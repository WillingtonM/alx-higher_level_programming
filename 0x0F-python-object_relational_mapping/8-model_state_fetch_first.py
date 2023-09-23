#!/usr/bin/python3
"""
script list first State object from database
"""

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
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
    frst_state = sess.query(State).order_by(State.id).first()
    if frst_state is not None:
        print("{}: {}".format(frst_state.id, frst_state.name))
    else:
        print("Nothing")
    sess.close()
