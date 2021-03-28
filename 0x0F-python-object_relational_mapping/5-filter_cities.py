#!/usr/bin/python3
"""
Lists all cities from the database hbtn_0e_4_usa
with name of state
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    cursor = db.cursor()
    cursor.execute("SELECT cities.name FROM cities \
    JOIN states ON cities.state_id = states.id WHERE states.name LIKE %s \
    ORDER BY cities.id ASC", (argv[4],))
    rows = cursor.fetchall()
    for row in rows
    print(row)
    
