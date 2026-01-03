from exception import UserNotFoundException, UserNotCorrectPasswordException
from models.user import UserProfile
from repository.user import UserRepository
from schema.user import UserLoginShema
from dataclasses import dataclass


@dataclass
class AuthService:
    user_repository: UserRepository

    def login(self, username: str, password: str) -> UserLoginShema:
        user = self.user_repository.get_user_by_username(username)
        self._validate_auth_user(user, password)

        return UserLoginShema(user_id=user.id, access_token=user.access_token)

    @staticmethod
    def _validate_auth_user(user: UserProfile, password: str):
        if not user:
            raise UserNotFoundException

        if user.password != password:
            raise UserNotCorrectPasswordException

