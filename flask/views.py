from flask import render_template, request, redirect, url_for
import json
import random
from app import app
from forms import *


with open("data.json") as f:
    data = json.loads(f.read())

@app.route("/")
def index():
	random.shuffle(data["teachers"])
	new_data = {"goals" : data["goals"], "teachers" : data["teachers"][:6], "goals_emoji" : data["goals_emoji"]}
	return render_template("index.html", **new_data)

@app.route("/goals/<goal>/")
def goal(goal):
	new_data = {
		"teachers" : [],
		"goal" : data["goals"].get(goal).lower(),
		"goal_emoji" : data["goals_emoji"][goal]
	}
	for e in data["teachers"]:
		if goal in e["goals"]:
			new_data["teachers"].append(e)
	return render_template("goal.html", **new_data)

@app.route("/profiles/<int:teacher_id>/")
def profile(teacher_id):
	for e in data["teachers"]:
		if e["id"] == teacher_id:
			teacher = e
			break
	new_data = {"goals" : data["goals"], "teacher" : teacher, "days" : data["days"], "goals_emoji":data["goals_emoji"]}
	return render_template("profile.html", **new_data)

@app.route("/request/", methods=["GET", "POST"])
def request():
	form = RequestForm()
	return render_template("request.html", form=form)

@app.route("/request_done/", methods=["GET", "POST"])
def request_done():
	form = RequestForm()
	if form.validate_on_submit():
		new_data = {
			"goal" : form.goal.data,
			"time" : data["time"].get(form.time.data),
			"name" : form.name.data,
			"phone" : form.phone.data
		}
		with open("request.json", 'r') as f:
		    request_data = json.loads(f.read())
		request_data["request_orders"].append(new_data)
		with open('request.json', 'w') as f:
			f.write(json.dumps(request_data))
		return render_template("request_done.html", **new_data, goals=data["goals"])
	else:
		return "errs"
	

@app.route("/booking/<int:teacher_id>/<day>/<int:time>/", methods=["GET","POST"])
def booking(teacher_id, day, time):
	for e in data["teachers"]:
		if e["id"] == teacher_id:
			teacher = e
			break
	new_data = {"goals" : data["goals"], "teacher" : teacher, "day" : day, "time" : str(time)+":00", "days" : data["days"]}
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