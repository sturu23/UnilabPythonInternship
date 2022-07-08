from app import db


class Student(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(24), nullable=False)
    surname = db.Column(db.String(24), nullable=False)
    teacher_id = db.Column(db.Integer,db.ForeignKey('teacher.id'))
    connection = db.relationship('Teacher',secondary='director')

    def __init__(self,name,surname):
        self.name = name
        self.surname = surname

class Teacher(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(24),nullable=False)
    students = db.relationship('Student',backref='teacher')


    def __init__(self,name):
        self.name = name

class Director(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    teacher_id = db.Column(db.Integer, db.ForeignKey('teacher.id'))
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'))

