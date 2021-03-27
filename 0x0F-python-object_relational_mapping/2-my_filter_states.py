#!/usr/bin/python3
"""
Script that lists all states from the
database hbtn_0e_0_usa.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Access to the database and get states
    """
    db = MySQLdb.connect(host="localhost", port=3306, 
                         user=argv[1], passwd=argv[2], 
                         db=argv[3], charset="utf8")
    
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE '{:s}' ORDER BY id ASC".format(argv[4]))
    rows = cursor.fetchall()
    for row in rows:
        print (row)
