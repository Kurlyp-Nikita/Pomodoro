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


@router.post(
    "/",
    response_model=Task
)
async def create_task(task: Task):
    fixture_tasks.append(task)
    return task


@router.patch(
    "/{task_id}",
    response_model=Task
)
async def update_task(task_id: int, name: str):
    for task in fixture_tasks:
        if task["id"] == task_id:
            task["name"] = name
            return task
