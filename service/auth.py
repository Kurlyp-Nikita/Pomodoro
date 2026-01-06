from client.google import GoogleClient
from exception import UserNotFoundException, UserNotCorrectPasswordException, TokenExpired, TokenNotCorrect
from models.user import UserProfile
from repository.user import UserRepository
from schema.user import UserLoginShema
from dataclasses import dataclass
from jose import jwt, JWTError
from datetime import timedelta
import datetime as dt
from settings import Settings


@dataclass
class AuthService:
    user_repository: UserRepository
    settings: Settings
    google_client: GoogleClient

    def google_auth(self, code: str) -> str:
        user_data = self.google_client.get_user_info(code)
        return user_data['access_token']

    def get_google_redirect_url(self) -> str:
        return self.settings.google_auth_redirect_url

    def login(self, username: str, password: str) -> UserLoginShema:
        user = self.user_repository.get_user_by_username(username)
        self._validate_auth_user(user, password)
        access_token = self.generate_access_token(user_id=user.id)
        return UserLoginShema(user_id=user.id, access_token=access_token)

    @staticmethod
    def _validate_auth_user(user: UserProfile, password: str):
        if not user:
            raise UserNotFoundException

        if user.password != password:
            raise UserNotCorrectPasswordException

    def generate_access_token(self, user_id: int) -> str:
        expires_data = (dt.datetime.now(dt.UTC) + timedelta(days=7)).timestamp()
        token = jwt.encode(
            {'user_id': user_id, 'expire': expires_data},
            self.settings.JWT_SECRET_KEY,
            algorithm=self.settings.JWT_ENCODE_ALGORITHM
        )
        return token

    def get_user_id_from_access_token(self, access_token: str) -> int:
        try:
            payload = jwt.decode(
                access_token,
                self.settings.JWT_SECRET_KEY,
                algorithms=[self.settings.JWT_ENCODE_ALGORITHM]
            )
        except JWTError:
            raise TokenNotCorrect

        if payload['expire'] < dt.datetime.now(dt.UTC).timestamp():
            raise TokenExpired

        return payload['user_id']
