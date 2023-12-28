# Разработать API для управления списком пользователей с использованием базы данных SQLite. Для этого создайте модель User со следующими полями:
# - id: int (идентификатор пользователя, генерируется автоматически)
# - username: str (имя пользователя)
# - email: str (электронная почта пользователя)
# - password: str (пароль пользователя)

# API должно поддерживать следующие операции:
# - Получение списка всех пользователей: GET /users/
# - Получение информации о конкретном пользователе: GET /users/{user_id}/
# - Создание нового пользователя: POST /users/
# - Обновление информации о пользователе: PUT /users/{user_id}/
# - Удаление пользователя: DELETE /users/{user_id}/

# Для валидации данных используйте параметры Field модели User. Для работы с базой данных используйте SQLAlchemy и модуль databases.


from contextlib import asynccontextmanager
from fastapi import FastAPI
import databases
from sqlalchemy import create_engine, delete, insert, update, select

from pydantic_models import UserIn, UserOut
from sqlalchemy_models import User as SUser, Base


DATABASE_URL = 'sqlite:///task_1.sqlite'
database = databases.Database(DATABASE_URL)

engine = create_engine(DATABASE_URL, connect_args={'check_same_thread': False})

Base.metadata.create_all(bind = engine)


@asynccontextmanager
async def lifespan(app: FastAPI):
    await database.connect()
    
    yield
    
    await database.disconnect()


app = FastAPI(lifespan=lifespan)


@app.get('/', response_model=list[UserOut])
async def index():
    users = select(SUser)
    
    return await database.fetch_all(users) 


@app.post('/users/', response_model=UserIn)
async def create_user(user: UserIn):
    new_user = insert(SUser).values(**user.model_dump())
    await database.execute(new_user)
    
    return new_user
    
    
@app.get('/users/{id}', response_model=UserOut)
async def get_user(id: int):
    user = await database.fetch_one(select(SUser))
    
    return user


@app.put('/users/{id}', response_model=UserOut)
async def update_user(id: int, new_user: UserIn):
    update_user =  (
        update(SUser)
        .where(SUser.id == id)
        .values(**new_user.model_dump())
    )
    await database.execute(update_user)
    
    return await database.fetch_one(select(SUser).where(SUser.id == id))  


@app.delete('/users/{id}')
async def delete_user(id: int):
    deleted_user = delete(SUser).where(SUser.id == id)
    
    await database.execute(deleted_user)
    
    return {'result': 'success', 'deleted_user_id': id}