#!/usr/bin/python3
"""
a script that lists all cities from the database hbtn_0e_4_usa
"""
if __name__ == "__main__":

    import MySQLdb
    from sys import argv

    try:
        connection = MySQLdb.connect(host="localhost", user=argv[1],
                                     passwd=argv[2], db=argv[3])
        cursor = connection.cursor()
        cursor.execute("SELECT cities.id, cities.name, states.name "
                       "FROM cities "
                       "RIGHT JOIN states ON states.id = cities.state_id "
                       "ORDER BY cities.id ASC")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except MySQLdb.Error as e:
        print(f"MySQLdb Erro: {e}")
    finally:
        cursor.close()
        connection.close()
