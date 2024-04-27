from dataclasses import dataclass
from models import User


@dataclass
class UserRepository:

    def create_user(self, username: str, password: str) -> User:
        pass