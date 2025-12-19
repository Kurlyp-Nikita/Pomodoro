from fastapi import APIRouter, status
from schema.task import Task
from fixtures import tasks as fixture_tasks
from database import get_db_connection

router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.get(
    "/all",
    response_model=list[Task]
)
async def get_tasks():
    cursor = get_db_connection().cursor()
    tasks = cursor.execute("SELECT * FROM Tasks").fetchall()

    result_tasks = []
    for task in tasks:
        task_dict = {
            "id": task[0],
            "name": task[1],
            "pomodoro_count": task[2],
            "category_id": task[3],
        }
        result_tasks.append(task_dict)
    return result_tasks


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


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(task_id: int):
    for index, task in enumerate(fixture_tasks):
        if task["id"] == task_id:
            del fixture_tasks[index]
            return {"message": "task delete"}
    return {"message": "task not found"}
