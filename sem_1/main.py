# Напишите простое веб-приложение на Flask, которое будет выводить на экран текст "Hello, World!".

from flask import Flask, render_template


app = Flask(__name__)

# Напишите простое веб-приложение на Flask, которое будет выводить на экран текст "Hello, World!".
@app.route('/')
def index():
    # return 'Hello, World!'
    return render_template('index.html')


# Добавьте две дополнительные страницы в ваше веб-приложение: страницу "about" и страницу "contact".

# Создать базовый шаблон для всего сайта, содержащий общие элементы дизайна (шапка, меню, подвал),
# и дочерние шаблоны для каждой отдельной страницы. Например, создать страницу "О нас" и "Контакты", 
# используя базовый шаблон.

@app.route('/about/')
def about():
    # return 'That\'s page about company'
    return render_template('about.html')


@app.route('/contacts/')
def contacts():
    # return 'Our contacts: company@mail.com'
    return render_template('contacts.html')


# Написать функцию, которая будет принимать на вход два числа и выводить на экран их сумму.
@app.route('/<int:num1>/<int:num2>/')
def Sum_to_n(num1: int, num2: int):
    return f'{num1} + {num2} = {num1 + num2}'


# Написать функцию, которая будет принимать на вход строку и выводить на экран ее длину.
@app.route('/<string:text>/')
def length(text: str):
    return f'{len(text)}'



# Написать функцию, которая будет выводить на экран HTML страницу с заголовком "Моя первая HTML страница" и абзацем "Привет, мир!".
@app.route('/')
def start():
    return f'<h1> Моя первая HTML страница </h1> <p> Привет, мир! </p>'


# Написать функцию, которая будет выводить на экран HTML страницу с таблицей, содержащей информацию о студентах. 
# Таблица должна содержать следующие поля: "Имя", "Фамилия", "Возраст", "Средний балл". 
# Данные о студентах должны быть переданы в шаблон через контекст.

@app.route('/table/')
def table():
    context = [
        {'name': 'Иван',
        'last_name': 'Иванов',
        'age' : 24},
        {'name': 'Пётр',
        'last_name': 'Петров',
        'age' : 48},
        {'name': 'Сергей',
        'last_name': 'Сидоров',
        'age' : 30},
        {'name': 'Мария',
        'last_name': 'Серова',
        'age' : 27},
    ]

    return render_template('table.html', context=context)




# Создать базовый шаблон для интернет-магазина, содержащий общие элементы дизайна (шапка, меню, подвал), 
# и дочерние шаблоны для страниц категорий товаров и отдельных товаров. 
# Например, создать страницы «Одежда», «Обувь» и «Куртка», используя базовый шаблон.

@app.route('/shoes/')
def shoes():
    return render_template('shoes.html')


@app.route('/clothes/')
def clothes():
    return render_template('clothes.html')


@app.route('/jacket/')
def jacket():
    return render_template('jacket.html')




if __name__ == '__main__':
    app.run(debug=True) 