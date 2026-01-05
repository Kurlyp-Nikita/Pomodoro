from fastapi import APIRouter, Depends
from typing import Annotated

from starlette import status

from repository.cache_tasks import TaskCache
from repository.task import TaskRepository
from schema.task import TaskShema, TaskCreateSchema
from dependencies import get_tasks_service, get_tasks_repository, get_tasks_cache_repository, get_request_user_id
from service.task import TaskService

router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.get(
    "/all",
    response_model=list[TaskShema]
)
async def get_tasks(
        task_service: Annotated[TaskService, Depends(get_tasks_service)]
):
    return task_service.get_tasks()


@router.post("/", response_model=TaskShema)
async def create_task(
        body: TaskCreateSchema,
        task_service: Annotated[TaskService, Depends(get_tasks_service)],
        user_id: int = Depends(get_request_user_id)
):
    task = task_service.create_task(body, user_id)
    return task


@router.patch(
    "/{task_id}",
    response_model=TaskShema
)
async def update_task(
        task_id: int,
        name: str,
        task_service: Annotated[TaskService, Depends(get_tasks_service)],
        user_id: int = Depends(get_request_user_id)
):
    return task_service.update_task_name(task_id=task_id, name=name, user_id=user_id)

@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(
        task_id: int,
        task_repository: Annotated[TaskRepository, Depends(get_tasks_repository)]
):
    task_repository.delete_task(task_id)
    return {"message": "task deleted successfully"}