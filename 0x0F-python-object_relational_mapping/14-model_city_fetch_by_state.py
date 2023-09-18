#!/usr/bin/python3
"""
 prints all City objects from the database
"""


if __name__ == '__main__':
    import sqlalchemy
    from sys import argv
    from model_state import Base, State
    from model_city import City
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    engine = create_engine(
        f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}'
    )

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    rows = session.query(City, State).filter(City.id == State.id)\
                                     .order_by(City.id).all()

    for city, state in rows:
        print(f'{state.name}: ({city.id}) {city.name}')
    session.close()
