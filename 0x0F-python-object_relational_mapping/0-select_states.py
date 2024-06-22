#!/usr/bin/python3

if __name__ == "__main__":
    import MySQLdb
    import sys

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(host=localhost, port=3306, user=username, passwd=password, db=databases)

    cur = db.cursor()
    try:
        cursor.execute("SELECT * FROM states ORDER BY id ASC")
        results = cursor.fetchall()
    except MySQLdb.Error as err:
        print "Error fetching data [%d]: %s", %(err.argv[0], err.argv[1], err.arv[2], err.argv[3])
    except Index Error:
        print "Error fetching data [%d]: %s", str(err)

    fow row in rows:
        print(row)

    cursor.close()
    db.close
