# База данных должна состоять из трёх таблиц: товары, заказы и пользователи.
# — Таблица «Товары» должна содержать информацию о доступных товарах, их описаниях и ценах.
# — Таблица «Заказы» должна содержать информацию о заказах, сделанных пользователями.
# — Таблица «Пользователи» должна содержать информацию о зарегистрированных пользователях магазина.

# • Таблица пользователей должна содержать следующие поля: id (PRIMARY KEY), имя, фамилия, адрес электронной почты и пароль.

# • Таблица заказов должна содержать следующие поля: id (PRIMARY KEY), 
# id пользователя (FOREIGN KEY), id товара (FOREIGN KEY), дата заказа и статус заказа.

# • Таблица товаров должна содержать следующие поля: id (PRIMARY KEY), название, описание и цена.

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Float, ForeignKey, Integer, String, Column, create_engine, Date, Boolean
from sqlalchemy.orm import relationship

Base = declarative_base()

class Goods(Base):
    __tablename__ = 'goods'
    
    id = Column(Integer, primary_key=True)
    orders = relationship('Orders', backref='goods')
    good_name = Column(String(25), nullable=False)
    description = Column(String(150))
    cost = Column(Float, nullable=False)


class Users(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    orders = relationship('Orders', backref='users')
    name = Column(String(30), nullable=False)
    last_name = Column(String(30), nullable=False)
    email = Column(String(30), nullable=False)
    password = Column(String(30), nullable=False) 

class Orders(Base):
    __tablename__ = 'orders'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    good_id = Column(Integer, ForeignKey('goods.id'), nullable=False)
    date_of_order = Column(Date, nullable=False)    
    status = Column(Boolean())
    
    
    
    