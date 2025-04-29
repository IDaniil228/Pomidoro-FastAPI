from fastapi import APIRouter, Depends

from Schema.UserSchema import UserSchema
from dependencies import get_users_service

from fixtures import tasks as fixtures_tasks

from db import get_db_session
from service import UserService

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/all", response_model=list[UserSchema])
def get_users(
        user_service : UserService = Depends(get_users_service)
):
    return user_service.get_users()



@router.post("/", response_model=list[UserSchema])
def create_user(user: UserSchema):
    fixtures_tasks.append(user)
    return fixtures_tasks


@router.patch("/update", response_model=UserSchema)
def edit_user(user_id: int, new_name: str):
    user = None
    with get_db_session() as connect:
        connect.execute(f"UPDATE Users SET name = ? WHERE id = ?", (new_name, user_id)).fetchone()
        connect.commit()
        user = connect.execute(f"SELECT * FROM Users WHERE id = ?", f"{user_id}").fetchone()
        if user is None:
            raise ValueError("Пользователь не найден")
        return UserSchema(
            id=user[0],
            name=user[1],
            age=user[2]
        )
