# Создать API для управления списком задач.
# Каждая задача должна содержать поля "название",
# "описание" и "статус" (выполнена/не выполнена).
# API должен позволять выполнять CRUD операции с
# задачами.


from contextlib import asynccontextmanager
from fastapi import FastAPI
import databases
from sqlalchemy import create_engine, delete, insert, update, select

from pydantic_models import TaskIn, TaskOut
from sqlalchemy_models import Base, Task


DATABASE_URL = 'sqlite:///tasks.sqlite'
database = databases.Database(DATABASE_URL)

engine = create_engine(DATABASE_URL, connect_args={'check_same_thread': False})

Base.metadata.create_all(bind = engine)


@asynccontextmanager
async def lifespan(app: FastAPI):
    await database.connect()
    
    yield
    
    await database.disconnect()


app = FastAPI(lifespan=lifespan)


@app.get('/', response_model=list[TaskOut])
async def index():
    tasks = select(Task)
    
    return await database.fetch_all(tasks)


@app.post('/tasks/')
async def create_task(new_task: TaskIn):
    task = insert(Task).values(**new_task.model_dump())
    await database.execute(task)
    
    return {'created': 'success'}


@app.get('/tasks/{id}', response_model=TaskOut)
async def get_task(id: int):
    task = await database.fetch_one(select(Task))
    
    return task


@app.put('/tasks/{id}')
async def update_task(id: int, new_task: TaskIn):
    updated_task = update(Task).where(Task.id == id).values(**new_task.model_dump())
    await database.execute(updated_task)
    
    return {'updated': 'success'}


@app.delete('/tasks/{id}')
async def delete_task(id:int):
    deleted_task = delete(Task).where(Task.id == id)
    await database.execute(deleted_task)
    
    return {'deleted': 'success', 'task id': id}
