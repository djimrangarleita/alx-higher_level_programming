#!/usr/bin/python3
"""
Start link class to table in database
"""
import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import City


def list_relationship():
    """Create single state"""
    if (len(sys.argv) != 4):
        return
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1],
                                   sys.argv[2],
                                   sys.argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).order_by(State.id):
        print(state.id, state.name, sep=': ')
        for city in state.cities:
            print('\t{}: {}'.format(city.id, city.name))

    session.close()


if __name__ == "__main__":
    list_relationship()
