from fastapi import APIRouter

router = APIRouter(prefix="/task", tags=["task"])

@router.get("/")
def ping():
    return {"massage" : "ok"}


@router.post("/create_task")
def create_task():
    return {"massage" : "ok"}