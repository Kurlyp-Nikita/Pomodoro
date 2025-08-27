from fastapi import FastAPI, APIRouter

router = APIRouter(prefix="/tasks", tags=["tasks"])

@router.get("/all")
async def get_tasks():
    return {"massage": "ok"}


@router.post("/")
async def create_tasks():
    return {"text": "app is working"}
