# Создать веб-приложение на FastAPI, которое будет предоставлять API для работы с 
# базой данных пользователей. 
# Пользователь должен иметь следующие поля:

# - ID (автоматически генерируется при создании пользователя)
# - Имя (строка, не менее 2 символов)
# - Фамилия (строка, не менее 2 символов)
# - Дата рождения (строка в формате "YYYY-MM-DD")
# - Email (строка, валидный email)
# - Адрес (строка, не менее 5 символов)

# API должен поддерживать следующие операции:

# 1. Добавление пользователя в базу данных
# 2. Получение списка всех пользователей в базе данных
# 3. Получение пользователя по ID
# 4. Обновление пользователя по ID
# 5. Удаление пользователя по ID

# Приложение должно использовать базу данных SQLite3 для хранения пользователей.


from contextlib import asynccontextmanager
from fastapi import FastAPI
import databases
from sqlalchemy import create_engine, delete, insert, update, select

from pydantic_models import UserIn, UserOut
from sqlalchemy_models import User2, Base


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
    users = select(User2)
    
    return await database.fetch_all(users) 


@app.post('/users/')
async def create_user(user: UserIn):
    new_user = insert(User2).values(**user.model_dump())
    await database.execute(new_user)
    
    return {'result': 'success'}
    
    
@app.get('/users/{id}', response_model=UserOut)
async def get_user(id: int):
    user = await database.fetch_one(select(User2))
    
    return user


@app.put('/users/{id}', response_model=UserOut)
async def update_user(id: int, new_user: UserIn):
    update_user =  (
        update(User2)
        .where(User2.id == id)
        .values(**new_user.model_dump())
    )
    await database.execute(update_user)
    
    return await database.fetch_one(select(User2).where(User2.id == id))  


@app.delete('/users/{id}')
async def delete_user(id: int):
    deleted_user = delete(User2).where(User2.id == id)
    await database.execute(deleted_user)
    
    return {'result': 'success', 'deleted_user_id': id}