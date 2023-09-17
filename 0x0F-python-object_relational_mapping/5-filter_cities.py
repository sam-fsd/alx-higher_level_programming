#!/usr/bin/python3
"""
a script that takes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa
"""

if __name__ == "__main__":

    import MySQLdb
    from sys import argv

    try:
        connection = MySQLdb.connect(host="localhost", user=argv[1],
                                     passwd=argv[2], port=3306,
                                     db=argv[3])
        cursor = connection.cursor()
        state_name = argv[4]
        cursor.execute("SELECT name FROM cities "
                       "WHERE state_id = "
                       "(SELECT id FROM states "
                       "WHERE name = '{}') "
                       "ORDER BY id ASC".format(state_name))

        results = cursor.fetchall()
        i = 0
        while i < len(results):
            print(results[i][0], end='')
            if i < (len(results) - 1):
                print(", ", end='')
            i += 1
        print()
    except MySQLdb.Error as e:
        print(f"MySQLdb Error: {e}")
    finally:
        cursor.close()
        connection.close()
