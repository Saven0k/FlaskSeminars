# База данных должна состоять из трёх таблиц: товары, заказы и пользователи.
# Создайте модели pydantic для получения новых данных и возврата существующих в БД для каждой из трёх таблиц.

from pydantic import BaseModel, Field

from datetime import date

# — Таблица «Заказы» должна содержать информацию о заказах, сделанных пользователями.
# Таблица заказов должна содержать следующие поля: id (PRIMARY KEY), 
# id пользователя (FOREIGN KEY), id товара (FOREIGN KEY), дата заказа и статус заказа.
class OrderIn(BaseModel):
    user_id: int
    good_id: int
    date_of_order: date
    status: bool = False

class OrderOut(OrderIn):
    id: int

    
    
# — Таблица «Товары» должна содержать информацию о доступных товарах, их описаниях и ценах.
# • Таблица товаров должна содержать следующие поля: id (PRIMARY KEY), название, описание и цена.
class GoodIn(BaseModel):
    good_name: str
    description: str
    cost: float
    
class GoodOut(GoodIn):
    id: int
    

# — Таблица «Пользователи» должна содержать информацию о зарегистрированных пользователях магазина.
# • Таблица пользователей должна содержать следующие поля: id (PRIMARY KEY), имя, фамилия, адрес электронной почты и пароль.
class UserIn(BaseModel):
    name: str
    last_name: str
    email: str
    password: str
    
class UserOut(UserIn):
    id: int