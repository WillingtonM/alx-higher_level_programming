#!/usr/bin/python3
"""
script lists all states from the database hbtn_0e_0_usa
"""

import MySQLdb_conn
from sys import argv

if __name__ == "__main__":
    db_conn = MySQLdb_conn.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db_conn=argv[3], charset="utf8")
    db_curs = db_conn.cursor()
    db_curs.execute("SELECT * FROM states ORDER BY id ASC")
    db_rows = db_curs.fetchall()
    for db_row in db_rows:
        print(db_row)
    db_curs.close()
    db_conn.close()
