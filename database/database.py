from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Тут подключение к базе данных

engine = create_engine("postgresql+psycopg2://postgres:password@localhost:5432/postgres")

Session = sessionmaker(engine)



def get_db_session() -> Session:
    return Session