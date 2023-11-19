#!/usr/bin/python3
"""adds a tate object"""

if __name__ == '__main__':
    from sqlalchemy import create_engine, Column, Integer
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State
    import sys

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    state1 = State(name="Louisiana")
    session.add(state1)
    session.commit()

    rows = session.query(State).filter(State.name=="Louisiana").order_by(State.id).all()

    for row in rows:
        print(row.id)
