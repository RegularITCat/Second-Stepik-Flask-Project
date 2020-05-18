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
	pprint.pprint(new_data)
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
	pprint.pprint(new_data)
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
	if form.validate_on_submit():
		name = form.name.data
		teacher = form.teacher.data
		phone = form.phone.data
		weekday = form.weekday.data
		time = form.time.data
		return render_template("booking_done.html", name=name, phone=phone, weekday=weekday, time=time)
	return render_template("booking.html", form=form, **new_data)

@app.route("/booking_done", methods=["GET","POST"])
def booking_done():
	new_data = {
			"name" : request.form["name"],
			"number" : request.form["number"],
			"weekday" : request.form["weekday"],
			"time" : request.form["time"]
		}
	return render_template("booking_done.html", **new_data)