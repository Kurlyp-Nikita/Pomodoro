from fastapi import APIRouter
from schema.task import Task
from fixtures import tasks as fixture_tasks

router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.get(
    "/all",
    response_model=list[Task]
)
async def get_tasks():
    return fixture_tasks



