from flask import Flask, render_template, url_for, request, redirect, flash, make_response
from werkzeug.utils import secure_filename

app = Flask(__name__)


# Создать страницу, на которой будет форма для ввода имени
# и электронной почты
# При отправке которой будет создан cookie файл с данными
# пользователя
# Также будет произведено перенаправление на страницу
# приветствия, где будет отображаться имя пользователя.
# На странице приветствия должна быть кнопка "Выйти"
# При нажатии на кнопку будет удален cookie файл с данными
# пользователя и произведено перенаправление на страницу
# ввода имени и электронной почты.


@app.route('/')
def index():
	return 'Hi!'

@app.route('/form/')
def form():
	name = request.form.get('name')
	email = request.form.get('email')

	response = make_response(render_template('form3.html', name=name, email=email))
	response.set_cookie(name, email)

	return response


if __name__ == '__main__':
    app.run(debug=True) 
