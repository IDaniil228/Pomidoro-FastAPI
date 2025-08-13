from fastapi import APIRouter, Depends

from Schema import UserCreateSchema
from Schema.UserLoginSchema import UserLoginSchema
from dependencies import get_users_service

from fixtures import tasks as fixtures_tasks

from db import get_db_session
from service import UserService

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/all", response_model=list[UserLoginSchema])
def get_users(
        user_service : UserService = Depends(get_users_service)
):
    return user_service.get_users()



@router.post("/", response_model=UserLoginSchema)
def create_user(body : UserCreateSchema, user_service :UserService = Depends(get_users_service)):
    return user_service.create_user(body.username, body.password)


@router.patch("/update", response_model=UserLoginSchema)
def edit_user(user_id: int, new_name: str):
    user = None
    with get_db_session() as connect:
        connect.execute(f"UPDATE Users SET name = ? WHERE id = ?", (new_name, user_id)).fetchone()
        connect.commit()
        user = connect.execute(f"SELECT * FROM Users WHERE id = ?", f"{user_id}").fetchone()
        if user is None:
            raise ValueError("Пользователь не найден")
        return UserLoginSchema(
            id=user[0],
            name=user[1],
            age=user[2]
        )
