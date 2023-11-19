#!/usr/bin/python3
"""module to print state and its cities"""

if __name__ == '__main__':
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from relationship_state import State
    from relationship_city import City
    import sys

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    state_names = session.query(State)

    for state in state_names:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("     {}: {}".format(city.id, city.name))
