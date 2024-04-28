from dataclasses import dataclass
from models import User
from sqlalchemy import insert, select
from sqlalchemy.orm import Session

@dataclass
class UserRepository:
    db_session: Session

    def create_user(self, username: str, password: str, access_token: str) -> User:
        query = insert(User).values(
            username=username,
            password=password,
            access_token=access_token
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