#!/usr/bin/python3
"""module to query states table"""
if __name__ == '__main__':
    from sqlalchemy import create_engine, Column, Integer, String
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy.ext.declarative import declarative_base
    import sys
    from model_state import Base, State

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    rows = session.query(State)

    for row in rows:
        print(str(row.id) + ":", row.name)
