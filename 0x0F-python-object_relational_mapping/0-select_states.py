#!/usr/bin/python3
""" defines a db(MySQL) connector """
if __name__ == "__main__":
    import sys
    import MySQLdb

    argv = sys.argv
    hostname = "localhost"
    port = 3306
    username = argv[1]
    password = argv[2]
    db = argv[3]

    try:
        db_conn = MySQLdb.connect(host=hostname, user=username,
                                  passwd=password, port=port, db=db)
        cursor = db_conn.cursor()
        cursor.execute("SELECT * FROM states ORDER BY id ASC")

        rows = cursor.fetchall()
    except MySQLdb.Error as e:
        print(f"Error occured {e}")

    for row in rows:
        print(row)

    cursor.close()
    db_conn.close()
