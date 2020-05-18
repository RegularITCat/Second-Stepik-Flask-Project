from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, validators

class BookingForm(FlaskForm):
	weekday = StringField("Вас зовут", [validators.InputRequired()])
	time = StringField("teacher_id", [validators.InputRequired()])
	teacher = IntegerField("teacher_id", [validators.InputRequired()])
	name = StringField("Вас зовут", [validators.InputRequired()])
	phone = IntegerField("Ваш телефон",[validators.InputRequired()])