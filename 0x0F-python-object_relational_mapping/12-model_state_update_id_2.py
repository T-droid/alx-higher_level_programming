#!/usr/bin/python3
"""updates table states"""

if __name__ == '__main__':
    from sqlalchemy import create_engine, Column, Integer
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State
    import sys

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.id == 2).first()

    if state:
        state.name = "New Mexico"
        session.commit()

    else:
        pass
