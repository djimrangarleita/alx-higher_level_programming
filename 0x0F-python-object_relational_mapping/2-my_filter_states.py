#!/usr/bin/python3
"""
List all states from db hbtn_0e_0_usa, conditional
"""
import MySQLdb
import sys


def get_states_with_condition():
    """Read and list states in db starting with 'N'"""
    uname = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    name = sys.argv[4]

    conn = MySQLdb.connect(host="localhost", port=3306, user=uname,
                           passwd=password, db=dbname, charset="utf8")

    cur = conn.cursor()
    cur.execute("SELECT * FROM states "
                "WHERE name = '{}' ORDER BY id ASC".format(name))
    query_rows = cur.fetchall()

    for row in query_rows:
        print(row)
    cur.close()
    conn.close()


if __name__ == '__main__':
    get_states_with_condition()
