from fastapi import FastAPI, APIRouter

router = APIRouter(prefix="/ping", tags=["ping-app, ping-db"])

@router.get("/db")
async def ping():
    return {"massage": "ok"}


@router.get("/app")
async def ping_app():
    return {"text": "app is working"}
