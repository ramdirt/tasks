from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Тут подключение к базе данных

engine = create_engine("sqlite:///tasks.sqlite")

Session = sessionmaker(engine)



def get_db_session() -> Session:
    return Session