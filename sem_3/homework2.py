# Задание №4
# Создайте форму регистрации пользователя с использованием Flask-WTF. Форма должна
# содержать следующие поля:
# ○ Имя пользователя (обязательное поле)
# ○ Электронная почта (обязательное поле, с валидацией на корректность ввода email)
# ○ Пароль (обязательное поле, с валидацией на минимальную длину пароля)
# ○ Подтверждение пароля (обязательное поле, с валидацией на совпадение с паролем)
# После отправки формы данные должны сохраняться в базе данных (можно использовать SQLite)
# и выводиться сообщение об успешной регистрации. Если какое-то из обязательных полей не
# заполнено или данные не прошли валидацию, то должно выводиться соответствующее
# сообщение об ошибке.

from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from flask_wtf.csrf import CSRFProtect
from forms_3 import RegisterForm
from models_4 import db, Users

app = Flask(__name__)
app.config['SECRET_KEY'] = b'e126ff82f9ade6b37daec524923984bf4ba76e0f23d8762bdedf18a6e64c8206'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///login.sqlite'
csrf = CSRFProtect(app)
db.init_app(app)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = RegisterForm()
    if request.method == 'POST' and form.validate():
        db.create_all()
        print('Created DB!')

        username = form.username.data   
        email = form.email.data
        password = form.password.data

        print(username, password, email)
        user = Users(username=username, email=email, password=password)

        db.session.add(user)
        db.session.commit()
        print('Db filled!')
    return render_template('login.html', form=form)