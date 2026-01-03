from schema.user import UserLoginShema
from dataclasses import dataclass


@dataclass
class AuthService:
    def login(self, username: str, password: str) -> UserLoginShema:
        pass

