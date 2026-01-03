from typing import Annotated
from fastapi import APIRouter, Depends
from dependencies import get_user_service
from schema.user import UserLoginShema, UserCreateShema
from service.user import UserService

router = APIRouter(prefix="/user", tags=["user"])


@router.post("", response_model=UserLoginShema)
async def create_user(body: UserCreateShema, user_service: Annotated[UserService, Depends(get_user_service)]):
    return user_service.create_user(body.username, body.password)

