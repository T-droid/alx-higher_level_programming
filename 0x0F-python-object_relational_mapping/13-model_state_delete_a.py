#!/usr/bin/python3
"""deletse state objects"""

if __name__ == '__main__':
    from sqlalchemy import create_engine, Integer, Column
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State
    import sys

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.name.like('%a%')).all()

    if state:
        for row in state:
            session.delete(row)
            session.commit()
