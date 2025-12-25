from redis import Redis
from schema.task import TaskShema


class CacheTask:
    def __init__(self, redis: Redis):
        self.redis = redis

    def get_task(self, task_id: int):
        pass

    def set_task(self, task: list[TaskShema]):
        task_json = [task.json() for task in task]
        self.redis.lpush('tasks', *task_json)

