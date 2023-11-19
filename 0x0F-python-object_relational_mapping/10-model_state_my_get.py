#!/usr/bin/python3
"""prints state object with name passed
as argument"""
if __name__ == '__main__':
    from sqlalchemy import create_engine, Column, Integer
    from sqlalchemy.orm import sessionmaker
    from model_state import State, Base
    import sys

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    var = sys.argv[4]

    rows = session.query(State).filter(State.name == var).order_by(State.id).all()

    if rows is None:
        print("Not Found")
    else:
        for row in rows:
            print(row.id)
