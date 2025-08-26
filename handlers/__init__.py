from handlers.ping import router as ping_router
from handlers.users import router as user_router
from handlers.auth import router as auth_router
from handlers.task import router as task_router

routers = [ping_router, user_router, auth_router, task_router]