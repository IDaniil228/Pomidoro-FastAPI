from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlite3 import connect

from setting import Setting




engine = create_engine("postgresql+psycopg2://hh:1234@localhost:5432/hh")

session = sessionmaker(engine)

def get_db_session():
    return session