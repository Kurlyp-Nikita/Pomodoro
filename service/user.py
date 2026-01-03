from dataclasses import dataclass
from schema.user import UserLoginShema


@dataclass
class UserService:
    user_repository = UserRepository

    def crete_user(self, username: str, password: str) -> UserLoginShema:
        user = self.user_repository.create_user(username, password)
        return UserLoginShema(user_id=user.id, access_token=user.access_token)

