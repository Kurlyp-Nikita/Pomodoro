from pydantic import BaseModel
from dataclasses import dataclass


@dataclass
class UserRepository(BaseModel):
    def create_user(self, username: str, password: str) -> User:
        pass

