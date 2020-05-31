from flask import render_template, redirect, url_for, abort
from app import app, db
from forms import *
from models import *
from sqlalchemy.orm.attributes import flag_modified
from sqlalchemy.exc import IntegrityError
from sqlalchemy.sql.expression import func


days = {"mon": "понедельник", "tue": "вторник", "wed": "среда",
        "thu": "четверг", "fri": "пятница", "sat": "суббота", "sun": "воскресенье"}
time_dict = {'time1': "1-2 часа", 'time2': "3-5 часов",
             'time3': "5-7 часов", 'time4': "7-10 часов"}


#@app.route("/db_test/")
#def db_test():
#    teacher = db.session.query(Teacher).get_or_404(0)
#    return render_template("db_test.html", teacher=teacher)


@app.route("/")
def index():
    teachers = db.session.query(Teacher).order_by(func.random()).limit(6)
    goals = db.session.query(Goal).all()
    return render_template("index.html", goals=goals, teachers=teachers)


@app.route("/goals/<goal>/")
def goal(goal):
    goal = db.session.query(Goal).filter(Goal.key == goal).first()
    if goal == None:
        abort(404)
    teachers_query = db.session.query(Teacher).all()
    teachers = []
    for teacher in teachers_query:
        if goal.id in [e.id for e in teacher.goals]:
            teachers.append(teacher)
    return render_template("goal.html", teachers=teachers,goal=goal)



@app.route("/profiles/<int:teacher_id>/")
def profile(teacher_id):
    teacher = db.session.query(Teacher).get_or_404(teacher_id)
    goals = db.session.query(Goal).all()
    return render_template("profile.html", teacher=teacher,days=days)


@app.route("/request/", methods=["GET", "POST"])
def request():
    form = RequestForm()
    if form.validate_on_submit():
        goal = form.goal.data
        time = time_dict[form.time.data]
        name = form.name.data
        phone = form.phone.data
        db.session.add(Request(goal=goal, time=time, name=name, phone=phone))
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            return redirect(url_for('profile', teacher_id=teacher_id))
        goal = db.session.query(Goal).filter(Goal.key == goal).first()
        return render_template("request_done.html", goal=goal, time=time, name=name, phone=phone)
    else:
        return render_template("request.html", form=form)


@app.route("/booking/<int:teacher_id>/<day>/<int:time>/", methods=["GET", "POST"])
def booking(teacher_id, day, time):
    form = BookingForm()
    teacher = db.session.query(Teacher).get_or_404(teacher_id)
    if teacher != None and day in days.keys() and time in range(0, 25, 2):
        time = str(time) + ":00"
        if teacher.free[day][time] == True:
            if form.validate_on_submit():
                name = form.name.data
                phone = form.phone.data
                db.session.add(Booking(day=day, time=time,
                                       teacher_id=teacher_id, name=name, phone=phone))
                teacher.free[day][time] = False
                flag_modified(teacher, 'free')
                try:
                    db.session.commit()
                except IntegrityError:
                    db.session.rollback()
                    return redirect(url_for('profile', teacher_id=teacher_id))
                new_data = {
                    "name": name,
                    "phone": phone,
                    "weekday": days[day],
                    "time": time,
                    "teacher_id": teacher.id
                }
                return render_template("booking_done.html", **new_data)
            else:
                return render_template("booking.html", form=form, teacher=teacher, day=days[day], time=time)
        else:
            return redirect(url_for('profile', teacher_id=teacher_id))
    abort(404)
