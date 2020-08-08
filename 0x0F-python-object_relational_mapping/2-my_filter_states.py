#!/usr/bin/python3
"""This script returns all data from db"""
import MySQLdb
from sys import argv
if __name__ == '__main__':
    user = argv[1]
    password = argv[2]  # Password: 1122
    database = argv[3]
    state_searched = str(argv[4])

    db = MySQLdb.connect(host="localhost", port=3306, user=user,
                         passwd=password, db=database)
    cur = db.cursor()
    my_text = "SELECT * FROM states WHERE name = " \
              + '\'' + state_searched + '\'' + " ORDER BY id ASC"
    cur.execute(my_text)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
