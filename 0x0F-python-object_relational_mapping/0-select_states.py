#!/usr/bin/python3
"""This script returns all data from db"""
import MySQLdb
from sys import argv
if __name__ == '__main__':
	user = argv[1]
	password = argv[2]
	database = argv[3]

	db = MySQLdb.connect(host="localhost", port=3306, user=user,
                             passwd=password, db=database)
	cur = conn.cursor()
	cur.execute("SELECT * FROM states ORDER BY is ASC")
	rows = cur.fetchall()
	for row in rows:
		print(row)
	cur.close()
	db.close()	
