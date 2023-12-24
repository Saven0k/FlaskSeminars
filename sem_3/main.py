from datetime import datetime

from flask import Flask, render_template
from models_1 import db, Student, Faculty
from models_2 import db, Author, Books
from random import randint, choice

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///authors.sqlite'
db.init_app(app)
@app.route('/')
def index():
    # students = Student.query.all()
    # context = {
    #     'students': students
    # }

    books = Books.query.all()
    context = {
        'books': books
    }
    return render_template('index.html', **context)

@app.cli.command('init-db')
def init_db():
    db.create_all()
    print('Created DB!')

#Model_1
# @app.cli.command('fill-db')
# def fill_db():
#     for i in range(5):
#         faculty = Faculty(faculty_name=f'Faculty {i + 1}')
#         db.session.add(faculty)
#         for g in range(3):
#             student = Student(name=f'Stundent {1 + g}', last_name='last name', age=randint(15, 35), gender=choice([True, False]),
#                               group='INF-1', faculty=faculty)
#             db.session.add(student)
#     db.session.commit()
#     print('db fills')


#Model_2
@app.cli.command('fill-db')
def fill_db():
    for i in range(5):
        author = Author(name=f'Author {i + 1}', last_name=f'Last name {i + 1}')
        db.session.add(author)
        for g in range(4):
            book = Books(
                name=f'Book {1 + g}',
                count=randint(1512, 352121), 
                author=author, 
                data_pub=randint(1900, 2023)
            )
            db.session.add(book)
    db.session.commit()
    print('db fills')


if __name__ == '__main__':
    app.run(debug=True)