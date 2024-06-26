#!/usr/bin/python3
"""
List all cities from db hbtn_0e_0_usa by states
"""
import MySQLdb
import sys


def get_all_cities_by_state():
    """Read and list of cities in db"""
    uname = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]

    conn = MySQLdb.connect(host="localhost", port=3306, user=uname,
                           passwd=password, db=dbname, charset="utf8")

    cur = conn.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name "
                "FROM cities JOIN states "
                "ON cities.state_id = states.id")
    query_rows = cur.fetchall()

    for row in query_rows:
        print(row)
    cur.close()
    conn.close()


if __name__ == '__main__':
    get_all_cities_by_state()
