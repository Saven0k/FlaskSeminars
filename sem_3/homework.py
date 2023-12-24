# Создать форму для регистрации пользователей на сайте. 
# Форма должна содержать поля "Имя", "Фамилия", "Email", "Пароль" и кнопку "Зарегистрироваться". 
# При отправке формы данные должны сохраняться в базе данных, а пароль должен быть зашифрован.

from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from flask_wtf.csrf import CSRFProtect
from forms_1 import RegisterForm
from models_3 import db, Users


app = Flask(__name__)
app.config['SECRET_KEY'] = b'e126ff82f9ade6b37daec524923984bf4ba76e0f23d8762bdedf18a6e64c8206'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Register.sqlite'
csrf = CSRFProtect(app)
db.init_app(app)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login-form', methods=['GET', 'POST'])
def login():
    form = RegisterForm()
    if request.method == 'POST' and form.validate():
        db.create_all()
        print('Created DB!')
        name = form.name.data
        email = form.email.data
        last_name = form.last_name.data
        password = form.password.data
        print(name, last_name, password, email)
        user = Users(name=name, last_name=last_name, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        print('Db filled!')
    return render_template('login.html', form=form)