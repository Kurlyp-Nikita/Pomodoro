from handlers.tasks import router as task_router
from handlers.ping import router as ping_router
from handlers.task import router as singular_task_router


routers = [task_router, singular_task_router, ping_router]
