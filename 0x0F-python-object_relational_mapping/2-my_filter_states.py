#!/usr/bin/python3
"""
Write a script that takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument."""

import sys
import MySQLdb

def main():
    conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            charset="utf8"
            )
    cur = conn.cursor()
    state_name = sys.argv[4]
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cur.execute(query,(state_name,))
    row = cur.fetchall()

    if row:
        for r in row:
            if r[1][0] == state_name
            print(r)
    else:
        print("No state found with the name '{}'".fomat(state_name))

    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
