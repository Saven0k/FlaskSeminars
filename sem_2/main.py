from flask import Flask, render_template, url_for, request, redirect, flash
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = b'9b7bc8ff7ff0eee6570722f500e9a214952797e4ff16224f9b7e4dda7fd1550'


# Создать страницу, на которой будет кнопка "Нажми меня", при нажатии на 
# которую будет переход на другую страницу с 
# приветствием пользователя по имени.


# @app.route('/')
# def index():
# 	data = {
# 		'name': 'Максим'
# 	}
# 	return render_template('index.html', **data)
 
# @app.route('/greet/<name>')
# def greet(name: str):
# 	return render_template('name.html', context=name)


# Создать страницу, на которой будет изображение и ссылка на другую страницу, 
# на которой будет отображаться форма для загрузки изображений.

# @app.route('/')
# def index():
# 	return render_template('index2.html')

# @app.route('/form', methods=['GET'])
# def form_get():
# 	return render_template('form.html')

# @app.route('/form/', methods=['POST'])
# def form_post():
# 	image = request.files.get('file')
# 	# file_name = secure_filename(image.filename)
# 	return redirect(url_for('index'))




# Создать страницу, на которой будет форма для ввода логина и пароля, 
# при нажатии на кнопку "Отправить" будет произведена проверка соответствия логина 
# и пароля и переход на страницу приветствия пользователя или страницу с ошибкой.


# @app.get('/')
# # def index():
# #     return render_template('login_form.html')


# @app.post('/login/')
# def login():
#     login = request.form.get('username')
#     password = request.form.get('password')

#     users_data = {'123': ('admin', 'admin')}

#     if (login, password) not in users_data.values():
#         print('Invalid user data!')
#         return redirect(url_for('index'))

#     return redirect(url_for('login_success', name=login))


# @app.route('/success/<name>')
# def login_success(name: str):
#     return render_template('name.html', context=name)




# Создать страницу, на которой будет форма для ввода текста и кнопка "Отправить", 
# при нажатии на которую будет 
# произведен подсчет количества слов в тексте и переход на страницу с результатом.


# @app.get('/')
# def index():
# 	return render_template('form.html')

# @app.post('/')
# def index_post():
# 	text = request.form.get('input')
# 	lenth = len(text.split())
# 	return render_template('form.html', text=text, lenth=lenth)




# Создать страницу, на которой будет форма для ввода двух чисел и выбор операции 
# (сложение, вычитание, умножение или деление) и кнопка "Вычислить", 
# при нажатии на которую будет произведено вычисление результата выбранной операции и
# переход на страницу с результатом.

"""
@app.get('/')
def index():
	return render_template('form.html')

@app.post('/')
def index_cucl():
	num1 = request.form.get('num1')
	num2 = request.form.get('num2')
	symbol = request.form.get('symbol')

	if symbol in '+-*/':
		result = eval(f'{num1}{symbol}{num2}')
	else:
		result = 'Ошибка!'

	text = f'{num1} {symbol} {num2}'
	return render_template('form.html', text=text, result=result)
"""






#                                   Домашенее задание



# Создать страницу, на которой будет форма для ввода числа
# и кнопка "Отправить"
# При нажатии на кнопку будет произведено
# перенаправление на страницу с результатом, где будет
# выведено введенное число и его квадрат.


# @app.get('/')
# def index():
# 	return render_template('form.html')

# @app.post('/')
# def square():
# 	if int(request.form.get('num')):
# 		num = int(request.form.get('num'))
# 		square = num ** 2
# 		return render_template('form.html', square=square, num=num)
# 	else:
# 		result = 'Ошибка!'
# 	return redirect(url_for('index'))




# Создать страницу, на которой будет форма для ввода имени
# и кнопка "Отправить"
# При нажатии на кнопку будет произведено
# перенаправление на страницу с flash сообщением, где будет
# выведено "Привет, {имя}!".


@app.get('/')
def index():
	return 'HI!'


@app.route('/login/', methods=['GET', 'POST'])
def login2():
	if request.method == 'POST':	
		name = request.form.get('name')
		flash(f'Привет, {name}', 'success')
		return redirect(url_for('login2'))
	return render_template('form2.html')	





if __name__ == '__main__':
    app.run(debug=True) 