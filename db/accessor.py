from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from setting import Setting



setting = Setting()

engine = create_engine(setting.db_url)

session = sessionmaker(engine)

def get_db_session():
    return session