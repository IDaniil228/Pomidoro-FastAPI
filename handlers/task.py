from fastapi import APIRouter, Depends

from typing import Annotated

from Schema.task import TaskSchema
from dependencies import get_request_user_id, get_task_service
from service.TaskService import TaskService

router = APIRouter(prefix="/task", tags=["task"])

@router.get("/", response_model=list[TaskSchema])
def get_tasks(
        task_service : Annotated[TaskService, Depends(get_task_service)],
        user_id : int = Depends(get_request_user_id)
):
    return task_service.get_tasks(user_id=user_id)


@router.post("/create_task", response_model=TaskSchema)
def create_task(
        title : str,
        task_service: Annotated[TaskService, Depends(get_task_service)],
        user_id: int = Depends(get_request_user_id)
):
    return task_service.create_task(title=title, user_id=user_id)