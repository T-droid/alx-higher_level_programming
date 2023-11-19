#!/usr/bin/python3
"""lists all state objects containing a"""

if __name__ == '__main__':
    from sqlalchemy import create_engine, Column, Integer
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State
    import sys

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    rows = session.query(State).order_by(State.id).filter(State.name.like('%a%'))

    for row in rows:
        print(str(row.id) + ":", row.name)
