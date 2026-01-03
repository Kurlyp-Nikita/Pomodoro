import string
from dataclasses import dataclass
from random import random, choices
from repository.user import UserRepository
from schema.user import UserLoginShema


@dataclass
class UserService:
    user_repository: UserRepository

    def crete_user(self, username: str, password: str) -> UserLoginShema:
        access_token = self._generate_access_token()
        user = self.user_repository.create_user(username, password, access_token)
        return UserLoginShema(user_id=user.id, access_token=user.access_token)

    @staticmethod
    def _generate_access_token() -> str:
        return ''.join(random.choices(string.ascii_uppercase + string.digits) for _ in range(10))
