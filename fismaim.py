from fastapi import FastAPI
from pydantic import BaseModel, Field, EmailStr, ConfigDict

app = FastAPI()

# Данные для тестирования
data = {
    "email": "abc@mail.ru",
    "bio": "Я пирожок",
    "age": 12,
}

data_wo_age = {
    "email": "abc@mail.ru",
    "bio": "Я пирожок",
    # "gender": "male",
    # "birthday": "2022"
}

class UserSchema(BaseModel):
    email: EmailStr
    bio: str | None = Field(max_length=10)

    model_config = ConfigDict(extra='forbid')

# Исправлено: создаем список для хранения пользователей
users = []  # было user = []

@app.post("/users")
def add_user(users_data: UserSchema):  # было users: UserSchema
    # Исправлено: добавляем users_data, а не users
    users.append(users_data)  # было user.append(user)
    return {"ok": True, "msg": "Юзер добавлен"}

@app.get("/users")
def get_users() -> list[UserSchema]:
    # Исправлено: возвращаем users (список пользователей)
    return users  # было return users (но users не был определен)



class UserAgeSchema(UserSchema):
    age: int = Field(ge=0, le=130)

# Теперь имя класса совпадает
print(repr(UserSchema(**data_wo_age)))


