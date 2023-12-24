# ������� ���� ������ ��� �������� ���������� � ������ � ����������.
# ���� ������ ������ ��������� ��� �������: "�����" � "������".
# � ������� "�����" ������ ���� ��������� ����: id, ��������, ��� �������, ���������� ����������� � id ������.
# � ������� "������" ������ ���� ��������� ����: id, ��� � �������.
# ���������� ������� ����� ����� ��������� "�����" � "������".
# �������� �������-����������, ������� ����� �������� ������ ���� ���� � ��������� �� �������.
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    books = db.relationship('Books', backref='author')
    name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    def __repr__(self) -> str:
        return f"Author({self.name})"

    def __str__(self) -> str:
        return f'{self.name}'


class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    date_pub = db.Column(db.Integer, nullable=False, default=datetime.now().year)
    count = db.Column(db.Integer, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=False)

    def __repr__(self) -> str:
        return f"Books({self.name}, {self.date_pub}, {self.count})"