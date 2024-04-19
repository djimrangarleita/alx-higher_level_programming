#!/usr/bin/python3
"""
Start link class to table in database
"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


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

    cities = session.query(City).order_by(City.id)
    for city in cities:
        print('{}: {} -> {}'.format(city.id, city.name, city.state.name))


if __name__ == "__main__":
    list_relationship()
