#!/usr/bin/python3
"""
    a script that lists all states with a name starting with N (upper N)
    from the database hbtn_0e_0_usa
"""
if __name__ == "__main__":

    import MySQLdb
    import sys

    hostname = 'localhost'
    password = sys.argv[2]
    username = sys.argv[1]
    db = sys.argv[3]
    port = 3306

    try:
        connection = MySQLdb.connect(host=hostname, user=username,
                                     passwd=password, db=db, port=port)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' "
                       "ORDER BY id ASC")
        results = cursor.fetchall()

        for result in results:
            print(result)
    except MySQLdb.Error as e:
        print("MySQLdb Error: %s".format(e))

    cursor.close()
    connection.close()
