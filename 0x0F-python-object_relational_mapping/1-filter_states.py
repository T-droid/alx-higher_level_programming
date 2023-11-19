#!/usr/bin/python3
"""
lists all states with name stating with N
"""
if __name__ == '__main__':
    import MySQLdb
    import sys

    username = sys.argv[1]
    password = sys.argv[2]

    db = sys.argv[3]

    conn = MySQLdb.Connection("localhost", username, password, db)

    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM states
        WHERE name
        LIKE 'N%'
        ORDER BY states.id ASC
        """)

    rows = cursor.fetchall()

    for row in rows:
        print(row)
    
    cursor.close()
    conn.close()
