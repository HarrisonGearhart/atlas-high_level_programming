#!/usr/bin/python3
"""lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cursr = db.cursor()
    cursr.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY states.id")
    rows = cursr.fetchall()
    for row in rows:
        print(row)
    cursr.close()
    db.close()