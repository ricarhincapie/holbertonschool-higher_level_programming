#!/usr/bin/python3
"""This script returns all data from db"""
import MySQLdb
from sys import argv
if __name__ == '__main__':
    user = argv[1]
    password = argv[2]  # Password: 1122
    database = argv[3]

    db = MySQLdb.connect(host="localhost", port=3306, user=user,
                         passwd=password, db=database)
    cur = db.cursor()
    my_text = "SELECT c.id, c.name, s.name FROM cities c \
               INNER JOIN states s on c.state_id = s.id"
    cur.execute(my_text)  # Here, a tuple needs to be used
    rows = cur.fetchall()  # The result
    for row in rows:
        print(row)
    cur.close()
    db.close()
