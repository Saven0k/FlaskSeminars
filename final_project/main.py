# Создайте модели pydantic для получения новых данных и возврата существующих в БД для каждой из трёх таблиц.
# Реализуйте CRUD операции для каждой из таблиц через создание маршрутов, REST API.

from contextlib import asynccontextmanager
from fastapi import FastAPI
import databases
from sqlalchemy import create_engine, delete, insert, update, select

from pydantic_models import UserIn, UserOut, GoodIn, GoodOut , OrderIn, OrderOut
from sqlalchemy_models import Base, Orders, Users, Goods

DATABASE_URL = 'sqlite:///Shop.sqlite'
database = databases.Database(DATABASE_URL)

engine = create_engine(DATABASE_URL, connect_args={'check_same_thread': False})

Base.metadata.create_all(bind = engine)


@asynccontextmanager
async def lifespan(app: FastAPI):
    await database.connect()
    
    yield
    
    await database.disconnect()
 

app = FastAPI(lifespan=lifespan)


# Таблица «Товары» должна содержать информацию о доступных товарах, их описаниях и ценах.
@app.get('/users', response_model=list[UserOut])
async def index():
    users = select(Users)
    
    return await database.fetch_all(users) 


@app.post('/users/')
async def create_user(user: UserIn):
    new_user = insert(Users).values(**user.model_dump())
    await database.execute(new_user)
    
    return {'result': 'success'}


@app.put('/users/{id}', response_model=UserOut)
async def update_user(id: int, new_user: UserIn):
    update_user =  (
        update(Users)
        .where(Users.id == id)
        .values(**new_user.model_dump())
    )
    await database.execute(update_user)
    
    return await database.fetch_one(select(Users).where(Users.id == id))  


@app.delete('/users/{id}')
async def delete_user(id: int):
    deleted_user = delete(Users).where(Users.id == id)
    await database.execute(deleted_user)
    
    return {'result': 'success', 'deleted_user_id': id}



# Таблица «Заказы» должна содержать информацию о заказах, сделанных пользователями.
@app.get('/goods', response_model=list[GoodOut])
async def index():
    goods = select(Goods)
    
    return await database.fetch_all(goods) 


@app.post('/goods/')
async def create_good(good: GoodIn):
    new_good = insert(Goods).values(**good.model_dump())
    await database.execute(new_good)
    
    return {'result': 'success'}

@app.put('/goods/{id}', response_model=GoodOut)
async def update_good(id: int, new_order: GoodIn):
    update_goods =  (
        update(Goods)
        .where(Goods.id == id)
        .values(**new_order.model_dump())
    )
    await database.execute(update_goods)
    
    return await database.fetch_one(select(Goods).where(Goods.id == id))  


@app.delete('/goods/{id}')
async def delete_good(id: int):
    deleted_good = delete(Goods).where(Goods.id == id)
    await database.execute(deleted_good)
    
    return {'result': 'success', 'deleted_good_id': id}



# Таблица «Пользователи» должна содержать информацию о зарегистрированных пользователях магазина.
@app.get('/orders', response_model=list[OrderOut])
async def index():
    orders = select(Orders)
    
    return await database.fetch_all(orders) 


@app.post('/orders/')
async def create_order(order: OrderIn):
    new_order = insert(Orders).values(**order.model_dump())
    await database.execute(new_order)
    
    return {'result': 'success'}


@app.put('/orders/{id}', response_model=OrderOut)
async def update_order(id: int, new_order: OrderIn):
    update_order =  (
        update(Orders)
        .where(Orders.id == id)
        .values(**new_order.model_dump())
    )
    await database.execute(update_order)
    
    return await database.fetch_one(select(Orders).where(Orders.id == id))  


@app.delete('/orders/{id}')
async def delete_order(id: int):
    deleted_order = delete(Orders).where(Orders.id == id)
    await database.execute(deleted_order)
    
    return {'result': 'success', 'deleted_order_id': id}
