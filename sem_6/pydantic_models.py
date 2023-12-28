#  Для этого создайте модель User со следующими полями:
# # - id: int (идентификатор пользователя, генерируется автоматически)
# # - username: str (имя пользователя)
# # - email: str (электронная почта пользователя)
# # - password: str (пароль пользователя)

from pydantic import BaseModel, Field

from datetime import date

"""

class UserIn(BaseModel):
    username: str
    email: str
    password: str


class UserOut(BaseModel):
    id: int
    username: str
    email: str
    password: str
 
"""
    
    
# - ID (автоматически генерируется при создании пользователя)
# - Имя (строка, не менее 2 символов)
# - Фамилия (строка, не менее 2 символов)
# - Дата рождения (строка в формате "YYYY-MM-DD")
# - Email (строка, валидный email)
# - Адрес (строка, не менее 5 символов)

class UserIn(BaseModel):
    name: str = Field(min_length=2)
    last_name: str = Field(min_length=2)
    email: str = Field()
    address: str = Field(min_length=5)
    data_of_bithday: date = Field(None)


class UserOut(UserIn):
    id: int
    
    
    
# Каждая задача должна содержать поля "название",
# "описание" и "статус" (выполнена/не выполнена).

class TaskIn(BaseModel):
    name: str
    description: str
    status: bool = False
    
    
class TaskOut(TaskIn):
    id:int