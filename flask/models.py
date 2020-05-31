from flask_sqlalchemy import SQLAlchemy
#from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.ext.mutable import MutableDict


db = SQLAlchemy()


class Booking(db.Model):
    __tablename__ = 'bookings'
    id = db.Column(db.Integer, primary_key=True)
    day = db.Column(db.String, nullable=False)
    time = db.Column(db.String, nullable=False)
    teacher_id = db.Column(db.Integer, db.ForeignKey(
        "teachers.id"), nullable=False)
    name = db.Column(db.String, nullable=False)
    phone = db.Column(db.String(11), nullable=False, unique=True)
    teacher = db.relationship('Teacher', back_populates='bookings')


class Request(db.Model):
    __tablename__ = 'requests'
    id = db.Column(db.Integer, primary_key=True)
    goal = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)
    phone = db.Column(db.String, nullable=False)
    time = db.Column(db.String, nullable=False)


teachers_goals_association = db.Table(
    "teachers_goals", db.metadata,
    db.Column("teacher_id", db.Integer, db.ForeignKey("teachers.id")),
    db.Column("goal_id", db.Integer, db.ForeignKey("goals.id"))
)


class Goal(db.Model):
    __tablename__ = 'goals'
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String, nullable=False)
    value = db.Column(db.String, nullable=False)
    emoji = db.Column(db.String, nullable=False)
    teachers = db.relationship(
        'Teacher', secondary=teachers_goals_association, back_populates='goals')


class Teacher(db.Model):
    __tablename__ = 'teachers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    about = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    picture = db.Column(db.String, nullable=False)
    price = db.Column(db.Float, nullable=False)
    goals = db.relationship(
        'Goal', secondary=teachers_goals_association, back_populates='teachers')
    free = db.Column(MutableDict.as_mutable(JSONB), nullable=False)
    bookings = db.relationship('Booking', back_populates='teacher')
