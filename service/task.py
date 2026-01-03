from dataclasses import dataclass

from repository.cache_tasks import TaskCache
from repository.task import TaskRepository
from schema.task import TaskShema


@dataclass
class TaskService:
    task_repository: TaskRepository
    task_cache: TaskCache

    def get_tasks(self) -> list[TaskShema]:

        if cache_task := self.task_cache.get_tasks():
            return cache_task

        else:
            tasks = self.task_repository.get_tasks()
            tasks_shema = [TaskShema.model_validate(task) for task in tasks]
            self.task_cache.set_task(tasks_shema)
            return tasks_shema
