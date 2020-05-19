from flask import render_template, request, redirect, url_for
import json
import pprint
from app import app
from forms import *


with open("data.json") as f:
    data = json.loads(f.read())

@app.route("/")
def index():
	new_data = {"goals" : data["goals"], "teachers" : ''}
	return render_template("index.html")

@app.route("/goals/<goal>/")
def goals(goal):
	return render_template("goal.html")

@app.route("/profiles/<int:teacher_id>/")
def profile(teacher_id):
	for e in data["teachers"]:
		if e["id"] == teacher_id:
			teacher = e
	new_data = {"goals" : data["goals"], "teacher" : teacher}
	return render_template("profile.html", **new_data)

@app.route("/request/")
def req():
	return render_template("request.html")

@app.route("/request_done/")
def request_done():
	return render_template("request_done.html")

@app.route("/booking/<int:teacher_id>/<day>/<int:time>/", methods=["GET","POST"])
def booking(teacher_id, day, time):
	for e in data["teachers"]:
		if e["id"] == teacher_id:
			teacher = e
	new_data = {"goals" : data["goals"], "teacher" : teacher, "day" : day, "time" : str(time)+":00"}
	form = BookingForm()
	return render_template("booking.html", form=form, **new_data)

@app.route("/booking_done/", methods=["GET","POST"])
def booking_done():
	form = BookingForm()
	if form.validate_on_submit():
		name = form.name.data
		teacher = form.teacher.data
		phone = form.phone.data
		weekday = form.weekday.data
		time = form.time.data
		new_data = {
			"name" : name,
			"phone" : phone,
			"weekday" : data["days"].get(weekday),
			"time" : time,
			"teacher" : teacher
		}
		#print(data["days"].get(request.form["weekday"]))
		for e in data['teachers']:
			if e["id"] == teacher:
				((e['free'])[weekday])[time] = False
		with open('data.json', 'w') as f:
			f.write(json.dumps(data))
		with open("booking.json", 'r') as f:
		    booking_data = json.loads(f.read())
		booking_data["booking_orders"].append(new_data)
		with open('booking.json', 'w') as f:
			f.write(json.dumps(booking_data))
		return render_template("booking_done.html", **new_data, )
	else:
		return "err"