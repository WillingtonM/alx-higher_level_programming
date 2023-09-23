#!/usr/bin/python3
"""
script that lists all states from database hbtn_0e_0_usa with given name
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db_conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    db_curs = db_conn.cursor()
    db_curs.execute("SELECT * FROM states WHERE name LIKE '{:s}' ORDER BY \
    id ASC".format(argv[4]))
    db_rows = db_curs.fetchall()
    for db_row in db_rows:
        if db_row[1] == argv[4]:
            print(db_row)
    db_curs.close()
    db_conn.close()
