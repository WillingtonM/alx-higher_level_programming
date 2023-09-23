#!/usr/bin/python3
"""
script lists cities from database hbtn_0e_4_usa with specified state name
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db_conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    cursor = db_conn.cursor()
    cursor.execute("SELECT cities.name FROM cities \
    JOIN states ON cities.state_id = states.id WHERE states.name LIKE %s \
    ORDER BY cities.id", (argv[4],))
    db_rows = cursor.fetchall()
    print(", ".join(db_city[0] for db_city in db_rows))
    cursor.close()
    db_conn.close()
