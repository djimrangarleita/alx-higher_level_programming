#!/usr/bin/python3
"""
Start link class to table in database
"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


def create_state():
    """Create single state"""
    if (len(sys.argv) != 4):
        return
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1],
                                   sys.argv[2],
                                   sys.argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    my_state = State(name='California')
    my_city = City(name='San Francisco', state=my_state)

    session.add(my_state)
    session.commit()


if __name__ == "__main__":
    create_state()
