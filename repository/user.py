from pydantic import BaseModel
from dataclasses import dataclass
from sqlalchemy import insert, select
from models.user import UserProfile
from sqlalchemy.orm import Session


@dataclass
class UserRepository(BaseModel):
    db_session: Session

    def create_user(self, username: str, password: str, access_token: str) -> UserProfile:
        query = insert(UserProfile).values(
            username=username,
            password=password,
            access_token=access_token,
        ).returning(UserProfile.id)

        with self.db_session() as session:
            user_id: int = session.execute(query).scalar()
            return self.get_user(user_id)

    def get_user(self, user_id: int) -> UserProfile | None:
        query = select(UserProfile).where(UserProfile.id == user_id)
        with self.db_session() as session:
            return session.execute(query).scalar_one_or_none()

