#!/usr/bin/python3
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3]
        ), pool_pre_ping=True)
    
    Session = sessionmaker(bind=engine)
    session = Session()

    states_To_delete = session.query(State).filter(State.name.like('%a%')).all()

    for state in states_To_delete:
        session.delete(state)

    session.commit()
    session.close()
