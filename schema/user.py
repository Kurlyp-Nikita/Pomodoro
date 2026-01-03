from pydantic import BaseModel


class UserLoginShema(BaseModel):
    user_id: int
    access_token: str

