from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, validators, RadioField


class BookingForm(FlaskForm):
    weekday = StringField("weekday", [validators.InputRequired()])
    time = StringField("teacher_id", [validators.InputRequired()])
    teacher = IntegerField("teacher_id", [validators.InputRequired()])
    name = StringField("Вас зовут", [validators.InputRequired(
        message="Необходимо указать имя. ")])
    phone = IntegerField("Ваш телефон", [validators.InputRequired(
        message="Необходимо указать номер телефона. ")])


class RequestForm(FlaskForm):
    goal = RadioField('Какая цель занятий?', choices=[("travel", "Для путешествий"), ("study", "Для учебы"), (
        "work", "Для работы"), ("relocate", "Для переезда"), ("program", "Для программирования")])
    time = RadioField('Сколько времение есть?', choices=[
                      ("time1", "1-2 часа"), ("time2", "3-5 часов"), ("time3", "5-7 часов"), ("time4", "7-10 часов")])
    name = StringField("Вас зовут", [validators.InputRequired(
        message="Необходимо указать имя. ")])
    phone = IntegerField("Ваш телефон", [validators.InputRequired(
        message="Необходимо указать номер телефона. ")])


class UserForm(FlaskForm):
    name = StringField("name", [validators.InputRequired(
        message="Необходимо указать имя. ")])
