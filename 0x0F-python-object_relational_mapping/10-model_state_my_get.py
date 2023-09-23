#!/usr/bin/python3
"""
script prints State object with name passed as argument from database
"""

import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sys import argv
from model_state import Base, State

if __name__ == "__main__":
    db_eng = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],
                                                                    argv[2],
                                                                    argv[3]))
    Base.metadata.create_all(db_eng)
    Session = sessionmaker(bind=db_eng)
    sess = Session()
    db_state = sess.query(State).filter_by(name=argv[4]).first()
    if db_state is not None:
        print(str(db_state.id))
    else:
        print("Not found")
    sess.close()
