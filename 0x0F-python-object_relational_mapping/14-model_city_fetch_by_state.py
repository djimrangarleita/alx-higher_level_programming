#!/usr/bin/python3
"""
Start link class to table in database
"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


def get_cities_by_state():
    """Print city names with state"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1],
                                   sys.argv[2],
                                   sys.argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(City).join(State).order_by(City.id)
    for city in cities:
        print('{}: ({}) {}'.format(city.state.name, city.id, city.name))


if __name__ == "__main__":
    get_cities_by_state()
