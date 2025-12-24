from typing import Annotated

from fastapi import APIRouter, status, Depends

from database.database import get_db_session
from repository.task import TaskRepository
from repository.task import get_tasks_repository
from schema.task import TaskShema

router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.get(
    "/all",
    response_model=list[TaskShema]
)
async def get_tasks(tasks_repository: Annotated[TaskRepository, Depends(get_tasks_repository)]):
    tasks = tasks_repository.get_tasks()
    return tasks


@router.post(
    "/",
    response_model=TaskShema
)
async def create_task(
        task: TaskShema,
        task_repository: Annotated[TaskRepository, Depends(get_tasks_repository)]
):
    task_id = task_repository.create_task(task)
    task.id = task_id
    return task


@router.patch(
    "/{task_id}",
    response_model=TaskShema
)
async def update_task(
        task_id: int,
        name: str,
        task_repository: Annotated[TaskRepository, Depends(get_tasks_repository)]
):
    return task_repository.update_task_name(task_id, name)

@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(
        task_id: int,
        task_repository: Annotated[TaskRepository, Depends(get_tasks_repository)]
):
    task_repository.delete_task(task_id)
    return {"message": "task deleted successfully"}
