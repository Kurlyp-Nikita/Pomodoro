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
    task_repository.create_task(task)
    return task


@router.patch(
    "/{task_id}",
    response_model=TaskShema
)
async def update_task(task_id: int, name: str):
    connection = get_db_session()
    cursor = connection.cursor()

    # Обновляем запись
    cursor.execute("UPDATE Tasks SET name=? WHERE id=?", (name, task_id))
    connection.commit()

    # Получаем обновленную запись (перед закрытием)
    cursor.execute("SELECT * FROM Tasks WHERE id=?", (task_id,))
    task = cursor.fetchone()
    connection.close()
    return TaskShema(
        id=task[0],
        name=task[1],
        pomodoro_count=task[2],
        category_id=task[3],
    )


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(task_id: int):
    connection = get_db_session()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM Tasks WHERE id=?", (task_id,))
    connection.commit()
    connection.close()
    return {"message": "task deleted successfully"}
