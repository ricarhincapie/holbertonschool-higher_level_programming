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
    WHERE state_id = (SELECT id FROM states WHERE name = %s) \
    ORDER BY id ASC"
    cur.execute(my_text, (state_searched,))  # Here, a tuple needs to be used

    begin = 0
    for row in cur.fetchall():
        if begin == 0:
            begin += 1
        else:
            print(", ", end='')
        print(row[0], end='')
    print()
    cur.close()
    db.close()
