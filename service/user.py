from dataclasses import dataclass
from schema.user import UserLoginShema


@dataclass
class UserService:
    def crete_user(self, username: str, password: str) -> UserLoginShema:
        pass

