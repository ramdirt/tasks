from dataclasses import dataclass
from models import User
from sqlalchemy import insert, select
from sqlalchemy.orm import Session

@dataclass
class UserRepository:
    db_session: Session

    def create_user(self, username: str, password: str) -> User:
        query = insert(User).values(
            username=username,
            password=password,
        ).returning(User.id)

        with self.db_session() as session:
            user_id: int = session.execute(query).scalar()
            session.flush()
            session.commit()

            return self.get_user(user_id)
        

    def get_user(self, user_id: int) -> User | None:
        query = select(User).where(User.id == user_id)

        with self.db_session() as session:
            user: User = session.execute(query).scalar_one_or_none()

        return user
    
    
    def get_user_by_username(self, username: str) -> User | None:
        query = select(User).where(User.username == username)

        with self.db_session() as session:
            user: User = session.execute(query).scalar_one_or_none()

        return user