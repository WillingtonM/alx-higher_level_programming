#!/usr/bin/python3
"""
script lists all states from database hbtn_0e_0_usa with a name starting with N
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db_conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    db_curs = db_conn.cursor()
    db_curs.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    db_rows = db_curs.fetchall()
    for db_row in db_rows:
        if db_row[1][0] == 'N':
            print(db_row)
    db_curs.close()
    db_conn.close()
