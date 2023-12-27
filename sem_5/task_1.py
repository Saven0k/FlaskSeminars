﻿# Создать API для управления списком задач. Приложение должно иметь возможность создавать, обновлять, удалять и получать список задач.
# ● Создайте модуль приложения и настройте сервер и маршрутизацию.
# ● Создайте класс Task с полями id, title, description и status.
# ● Создайте список tasks для хранения задач.
# ● Создайте маршрут для получения списка задач (метод GET).
# ● Создайте маршрут для создания новой задачи (метод POST).
# ● Создайте маршрут для обновления задачи (метод PUT).
# ● Создайте маршрут для удаления задачи (метод DELETE).
# ● Реализуйте валидацию данных запроса и ответа.

from fastapi import FastAPI
from pydantic_models import Task


app = FastAPI()
tasks: list[Task] = []


@app.get("/")
async def index():
    return tasks


@app.post("/tasks")
async def create_task(task: Task):
    tasks.append(task)
    return task
    
@app.put("/tasks/{task_id}")
async def update_task(task_id: int, new_task: Task):
    tasks[task_id] = new_task
    
    return {'updated': True, 'task': new_task}  
    

@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    filtered_task = [task for task in tasks if task.id == task_id]
    if not filtered_task: return {'deleted': False}

    task = filtered_task[0]
    
    tasks.remove(task)
    
    return {'deleted': True, 'task': task}  