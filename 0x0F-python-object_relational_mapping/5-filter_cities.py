#!/usr/bin/python3
"""
takes state as an argument and lists
all cities of the state
"""
if __name__ == '__main__':
    import MySQLdb
    import sys

    if len(sys.argv) != 5:
        print("Usage: <usernaem><password><database><statename>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    db = sys.argv[3]
    state_name = sys.argv[4]

    conn = MySQLdb.Connection("localhost", username, password, db)

    c = conn.cursor()

    query = """
        SELECT C.name
        FROM cities AS C
        INNER JOIN states AS S
        ON C.state_id = S.id
        WHERE S.name=%s
        ORDER BY C.id;
        """

    c.execute(query, (state_name,))

    rows = c.fetchall()

    city_names = [row[0] for row in rows]

    result = ", ".join(city_names)

    print(result)

    c.close()
    conn.close()
