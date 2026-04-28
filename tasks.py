from flask import Blueprint, render_template, request, redirect, url_for
from models import Task
from extensions import db
from flask_login import login_required, current_user
from datetime import date

tasks = Blueprint('tasks', __name__)

@tasks.route("/", methods=["GET"])
@login_required
def dashboard():
    search = request.args.get("search")
    priority = request.args.get("priority")
    status = request.args.get("status")

    query = Task.query.filter_by(user_id=current_user.id)

    if search:
        query = query.filter(Task.title.contains(search))

    if priority and priority != "All":
        query = query.filter_by(priority=priority)

    if status == "completed":
        query = query.filter_by(completed=True)
    elif status == "pending":
        query = query.filter_by(completed=False)

    tasks_list = query.all()

    total = Task.query.filter_by(user_id=current_user.id).count()
    completed = Task.query.filter_by(user_id=current_user.id, completed=True).count()
    pending = total - completed
    today = date.today()

overdue = Task.query.filter(
    Task.user_id == current_user.id,
    Task.due_date < today,
    Task.completed == False
).count()

due_today = Task.query.filter(
    Task.user_id == current_user.id,
    Task.due_date == today,
    Task.completed == False
).count()

    return render_template(
        "dashboard.html",
        tasks=tasks_list,
        total=total,
        completed=completed,
        pending=pending,
        overdue=overdue,
        due_today=due_today,
        current_date=str(date.today())
    )

@tasks.route("/add", methods=["POST"])
@login_required
def add_task():
    task = Task(
        title=request.form.get("title"),
        description=request.form.get("description"),
        due_date=request.form.get("due_date"),
        priority=request.form.get("priority"),
        user_id=current_user.id
    )
    db.session.add(task)
    db.session.commit()
    return redirect(url_for("tasks.dashboard"))

@tasks.route("/complete/<int:id>")
@login_required
def complete_task(id):
    task = Task.query.get(id)
    task.completed = not task.completed
    db.session.commit()
    return redirect(url_for("tasks.dashboard"))

@tasks.route("/delete/<int:id>")
@login_required
def delete_task(id):
    task = Task.query.filter_by(id=id, user_id=current_user.id).first()

    if task:
        db.session.delete(task)
        db.session.commit()

    return redirect(url_for("tasks.dashboard"))

@tasks.route("/edit/<int:id>", methods=["GET", "POST"])
@login_required
def edit_task(id):
    task = Task.query.get(id)

    if request.method == "POST":
        task.title = request.form.get("title")
        task.description = request.form.get("description")
        task.due_date = request.form.get("due_date")
        task.priority = request.form.get("priority")

        db.session.commit()
        return redirect(url_for("tasks.dashboard"))

    return render_template("edit_task.html", task=task)