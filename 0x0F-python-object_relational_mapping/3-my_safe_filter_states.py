#!/usr/bin/python3
"""
a script that takes in arguments and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument
safe from SQL injection
"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    try:
        connection = MySQLdb.connect(host="localhost", user=argv[1],
                                     passwd=argv[2], port=3306,
                                     db=argv[3])
        state_name = argv[4]
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM states WHERE name = %s "
                       "ORDER BY id ASC", (state_name,))
        results = cursor.fetchall()

        for row in results:
            if row[1] == state_name:
                print(row)
    except MySQL.Error as e:
        print(f"MySQLdb Error: {e}")
    finally:
        cursor.close()
        connection.close()
