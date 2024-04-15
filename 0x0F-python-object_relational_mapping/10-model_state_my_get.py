#!/usr/bin/python3
"""
Start link class to table in database
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


def get_state():
    """Read single state with name matching param"""
    if (len(sys.argv) != 5):
        return
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1],
                                   sys.argv[2],
                                   sys.argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    search = sys.argv[4]
    state = session.query(State).filter_by(name=f'{search}').first()
    if state:
        print(state.id)
    else:
        print('Not found')


if __name__ == "__main__":
    get_state()
