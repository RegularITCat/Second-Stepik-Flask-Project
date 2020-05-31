from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, validators, RadioField


class BookingForm(FlaskForm):
    name = StringField("Вас зовут", [validators.InputRequired(
        message="Необходимо указать имя. ")])
    phone = StringField("Ваш телефон", [validators.InputRequired(
        message="Необходимо указать номер телефона. "), validators.Length(min=11, message="Неккоректно указан номер телефона. ")])


class RequestForm(FlaskForm):
    goal = RadioField('Какая цель занятий?', choices=[("travel", "Для путешествий"), ("study", "Для учебы"), (
        "work", "Для работы"), ("relocate", "Для переезда"), ("program", "Для программирования")])
    time = RadioField('Сколько времение есть?', choices=[
                      ('time1', "1-2 часа"), ('time2', "3-5 часов"), ('time3', "5-7 часов"), ('time4', "7-10 часов")])
    name = StringField("Вас зовут", [validators.InputRequired(
        message="Необходимо указать имя. ")])
    phone = StringField("Ваш телефон", [validators.InputRequired(
        message="Необходимо указать номер телефона. "), validators.Length(min=11, message="Неккоректно указан номер телефона. ")])


class UserForm(FlaskForm):
    name = StringField("name", [validators.InputRequired(
        message="Необходимо указать имя. ")])
