#!/usr/bin/python3
"""
List all cities from db hbtn_0e_0_usa by states
"""
import MySQLdb
import sys


def get_all_cities_by_state_name():
    """Read and list of cities in db"""
    if len(sys.argv) != 5:
        return
    uname = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    state_name = sys.argv[4]

    conn = MySQLdb.connect(host="localhost", port=3306, user=uname,
                           passwd=password, db=dbname, charset="utf8")

    cur = conn.cursor()
    cur.execute("SELECT cities.name  AS city_name FROM cities\
            JOIN states ON cities.state_id = states.id\
            WHERE BINARY states.name = %s", (state_name,))
    cities = [row[0] for row in cur.fetchall()]
    city_string = ", ".join(cities)

    print(city_string)

    cur.close()
    conn.close()


if __name__ == '__main__':
    get_all_cities_by_state_name()
