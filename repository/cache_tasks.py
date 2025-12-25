import json
from redis import Redis
from schema.task import TaskShema


class TaskCache:
    def __init__(self, redis: Redis):
        self.redis = redis

    def get_task(self) -> list[TaskShema]:
        with self.redis as redis:
            task_json = redis.lrange("tasks", 0, -1)
            return [TaskShema.model_validate(json.loads(task)) for task in task_json]

    def set_task(self, task: list[TaskShema]):
        task_json = [task.json() for task in task]
        with self.redis as redis:
            redis.lpush('tasks', *task_json)

