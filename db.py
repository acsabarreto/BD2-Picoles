from contextlib import contextmanager
from typing import Generator
from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.orm import declarative_base

engine:Engine = create_engine('sqlite:///picoles.db')
DBSession:Session = sessionmaker(bind=engine, autoflush=False, expire_on_commit=False)
DBModel = declarative_base()

@contextmanager
def get_session() -> Generator:
    session:Session = DBSession()
    try:
        yield session
    finally:
        session.close()