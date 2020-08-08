#!/usr/bin/python3
"""This script returns all data from db"""
import MySQLdb
from sys import argv
if __name__ == '__main__':
    user = argv[1]
    password = argv[2]  # Password: 1122
    database = argv[3]
    state_searched = argv[4]

    db = MySQLdb.connect(host="localhost", port=3306, user=user,
                         passwd=password, db=database)
    cur = db.cursor()
    my_text = "SELECT name FROM cities \
    WHERE state_id = (SELECT id FROM states WHERE name = %s)"
    cur.execute(my_text, (state_searched,))  # Here, a tuple needs to be used
    rows = cur.fetchall()
    flag = 0
    for row in rows:
        flag = flag + 1
        if len(rows) == flag:
            print(row[0])
        else:
            print(row[0], end=", ")
    cur.close()
    db.close()
