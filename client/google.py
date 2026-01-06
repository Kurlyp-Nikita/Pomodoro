from dataclasses import dataclass
from os import access

from settings import Settings
import requests


@dataclass
class GoogleClient:
    settings: Settings


    def get_user_info(self, code: str) -> dict:
        access_token = self._get_user_access_token(code)
        user_info = requests.get(
            f'https://accounts.google.com/o/oauth2/v2/userinfo',
            headers={'Authorization': f'Bearer {access_token}'}
        )
        return user_info.json()


    def _get_user_access_token(self, code: str) -> dict:
        data = {
            'code': code,
            'client_id': self.settings.GOOGLE_CLIENT_ID,
            'client_secret': self.settings.GOOGLE_SECRET_KEY,
            'redirect_uri': self.settings.GOOGLE_REDIRECT_URI,
            'grant_type': 'authorization_code',
        }

        response = requests.post(self.settings.GOOGLE_TOKEN_URL, data=data)
        return response.json()
