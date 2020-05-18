from flask import render_template

from app import app


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/goals/<goal>/")
def goals(goal):
	return render_template("goal.html")

@app.route("/profiles/<teacher_id>/")
def goals(teacher_id):
	return render_template("profile.html")

@app.route("/request/")
def goals():
	return render_template("request.html")

@app.route("/request_done/")
def goals():
	return render_template("request_done.html")

@app.route("/booking/<teacher_id>/<day>/<time>/")
def goals(teacher_id, day, time):
	return render_template("booking.html")

@app.route("/booking_done/")
def goals():
	return render_template("booking_done.html")

