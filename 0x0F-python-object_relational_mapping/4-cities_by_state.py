#!/usr/bin/python3
"""
lists all cities from database
"""
if __name__ == '__main__':
    import MySQLdb
    import sys

    if len(sys.argv) != 4:
        print("Usage: <username><password><databasename>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    db = sys.argv[3]

    conn = MySQLdb.Connection("localhost", username, password, db)

    cursor = conn.cursor()

    query = """
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id;
        """

    cursor.execute(query)

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    conn.close()
