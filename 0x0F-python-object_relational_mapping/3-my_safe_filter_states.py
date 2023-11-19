#!/usr/bin/python3
"""
takes an argument and displays values
matching the argument
"""
if __name__ == '__main__':
    import MySQLdb
    import sys

    if len(sys.argv) != 5:
        print("Usage: <username><password><db_name><name_searched>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    db = sys.argv[3]
    state_name = sys.argv[4]

    conn = MySQLdb.Connection("localhost", username, password, db)

    cursor = conn.cursor()

    query = "SELECT * FROM states WHERE name=%s ORDER BY states.id ASC"
    cursor.execute(query, (state_name,))

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    conn.close()
