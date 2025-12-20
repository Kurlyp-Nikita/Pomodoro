from fastapi import APIRouter, status

from schema import task
from schema.task import Task
from fixtures import tasks as fixture_tasks
from database import get_db_connection

router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.get(
    "/all",
    response_model=list[Task]
)
async def get_tasks():
    result_tasks: list[Task] = []
    cursor = get_db_connection().cursor()
    tasks = cursor.execute("SELECT * FROM Tasks").fetchall()

    for task in tasks:
        result_tasks.append(Task(
            id=task[0],
            name=task[1],
            pomodoro_count=task[2],
            category_id=task[3],
        ))
    return result_tasks


@router.post(
    "/",
    response_model=Task
)
async def create_task(task: Task):
    conection = get_db_connection()
    cursor = conection.cursor()
    cursor.execute("INSERT INTO Tasks (name, pomodoro_count, category_id) VALUES (?, ?, ?)",
                   (task.name, task.pomodoro_count, task.category_id))
    conection.commit()
    conection.close()
    return task


@router.patch(
    "/{task_id}",
    response_model=Task
)
async def update_task(task_id: int, name: str):
    connection = get_db_connection()
    cursor = connection.cursor()

    # Обновляем запись
    cursor.execute("UPDATE Tasks SET name=? WHERE id=?", (name, task_id))
    connection.commit()

    # Получаем обновленную запись (перед закрытием)
    cursor.execute("SELECT * FROM Tasks WHERE id=?", (task_id,))
    task = cursor.fetchone()
    connection.close()
    return Task(
        id=task[0],
        name=task[1],
        pomodoro_count=task[2],
        category_id=task[3],
    )


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(task_id: int):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM Tasks WHERE id=?", (task_id,))
    connection.commit()
    connection.close()
    return {"message": "task deleted successfully"}
