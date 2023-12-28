#  Для этого создайте модель User со следующими полями:
# # - id: int (идентификатор пользователя, генерируется автоматически)
# # - username: str (имя пользователя)
# # - email: str (электронная почта пользователя)
# # - password: str (пароль пользователя)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, String, Column, create_engine, Date, Boolean


Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)
    
    
# - ID (автоматически генерируется при создании пользователя)
# - Имя (строка, не менее 2 символов)
# - Фамилия (строка, не менее 2 символов)
# - Дата рождения (строка в формате "YYYY-MM-DD")
# - Email (строка, валидный email)
# - Адрес (строка, не менее 5 символов)

class User2(Base):
    __tablename__ = 'user2'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    last_name = Column(String(29), nullable=False)
    email = Column(String(20), nullable=False) 
    address = Column(String(20), nullable=False)
    data_of_bithday = Column(Date, nullable=False)    
    
    
# Каждая задача должна содержать поля "название",
# "описание" и "статус" (выполнена/не выполнена).

class Task(Base):
    __tablename__ = 'Task'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(25))
    description = Column(String(150))
    status = Column(Boolean())