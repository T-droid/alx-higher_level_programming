#!/usr/bin/python3
"""module to fetch city objects"""

if __name__ == '__main__':
    from sqlalchemy import create_engine
    from model_city import City, Base
    from sqlalchemy.orm import sessionmaker
    import sys
    from model_state import State, Base

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    results = session.query(State, City).join(City, State.id == City.state_id).all()

    if results:
        for state, city in results:
            print("{}: ({}) {}".format(state.name, city.id, city.name))
