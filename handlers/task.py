from fastapi import APIRouter

router = APIRouter(prefix="/task", tags=["tasks"])


@router.post("/{task_id}")
async def create_task(task_id: str):
    return {"task_id": task_id}


