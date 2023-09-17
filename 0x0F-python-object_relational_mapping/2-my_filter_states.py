#!/usr/bin/python3
"""
     script that takes in an argument and displays all values
     in the states table of hbtn_0e_0_usa where
     name matches the argument
"""
if __name__ == "__main__":
    import sys
    import MySQLdb

    argv = sys.argv
    hostname = "localhost"
    port = 3306
    username = argv[1]
    password = argv[2]
    db = argv[3]
    search_term = argv[4]

    try:
        db_conn = MySQLdb.connect(host=hostname, user=username,
                                  passwd=password, port=port, db=db)
        cursor = db_conn.cursor()
        query = (
            "SELECT * FROM states WHERE name = '{}' "
            "ORDER BY id ASC".format(search_term)
        )
        cursor.execute(query)

        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except MySQLdb.Error as e:
        print(f"Error occured {e}")
    finally:
        cursor.close()
        db_conn.close()
