#    Необходимо создать API для управления списком задач. Каждая задача должна содержать заголовок и описание. 
# Для каждой задачи должна быть возможность указать статус (выполнена/не выполнена).
# API должен содержать следующие конечные точки:
# — GET /tasks — возвращает список всех задач.
# — GET /tasks/{id} — возвращает задачу с указанным идентификатором.
# — POST /tasks — добавляет новую задачу.
# — PUT /tasks/{id} — обновляет задачу с указанным идентификатором.
# — DELETE /tasks/{id} — удаляет задачу с указанным идентификатором.

# Для каждой конечной точки необходимо проводить валидацию данных запроса и ответа. Для этого использовать библиотеку Pydantic.


from fastapi import FastAPI, Query

from pydantic_models import Task


app = FastAPI()
tasks: list[Task] = []


# — GET /tasks — возвращает список всех задач.
@app.get('/tasks')
async def view_tasks():
    return tasks


# — GET /tasks/{id} — возвращает задачу с указанным идентификатором.
@app.get('/tasks/{id}')
async def search_task(id: int):
    filtered_tasks = [task for task in tasks if task.id == id]
    
    if not filtered_tasks:
        return {'search': False}

    return  filtered_tasks


# — POST /tasks — добавляет новую задачу.
@app.post('/tasks')
async def add_task(new_task: Task):
    tasks.append(new_task)
    return new_task


# — PUT /tasks/{id} — обновляет задачу с указанным идентификатором.
@app.put('/tasks/{id}')
async def update_task(id:int, new_task: Task):
    filtered_tasks = [task for task in tasks if task.id == id]
    
    if not filtered_tasks:
        return {'updated': False}
    
    task = filtered_tasks[0]
    
    task.description = new_task.description
    task.title = new_task.title
    task.status = new_task.status

    return  {'update': True, 'task': task}


# — DELETE /tasks/{id} — удаляет задачу с указанным идентификатором.
@app.delete('/tasks/{id}')
async def delete_task(id: int):
    filtered_tasks = [task for task in tasks if task.id == id]
    
    if not filtered_tasks:
        return {'deleted': False}
    
    task = filtered_tasks[0]
    tasks.remove(task)
    
    return  {'delete': True, 'task': task}

