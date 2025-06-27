#!/usr/bin/python3
"""List all City objects from the database hbtn_0e_101_usa with their corresponding State"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import City
from relationship_state import Base, State

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}',
        pool_pre_ping=True
    )
    
    Session = sessionmaker(bind=engine)
    session = Session()
    
    cities = session.query(City).order_by(City.id).all()
    
    for city in cities:
        print(f"{city.id}: {city.name} -> {city.state.name}")
    
    session.close()
