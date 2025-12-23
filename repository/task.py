from sqlalchemy import select
from sqlalchemy.orm import Session

from database.database import get_db_session
from database.models import Tasks


class TaskRepository:

    def __init__(self, db_session: Session):
        self.db_session = db_session

    def get_task(self, task_id: int):
        query = select(Tasks).where(Tasks.id == task_id)
        with self.db_session() as session:
            task = session.execute(query)
        return task

    def get_tasks(self):
        pass


def get_tasks_repository() -> TaskRepository:
    db_session = get_db_session()
    return TaskRepository(db_session)

