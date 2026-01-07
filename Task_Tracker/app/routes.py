from flask import Blueprint, render_template, redirect, url_for, request

from .models import Task
from . import db

main = Blueprint("main", __name__)


@main.route("/")
def index():
    tasks = Task.query.all()
    return render_template("index.html", tasks=tasks)


@main.route("/add", methods=["GET", "POST"])
def add_task():
    if request.method == "POST":
        title = request.form["title"]
        description = request.form.get("description", "")

        task = Task(title=title, description=description)
        db.session.add(task)
        db.session.commit()

        return redirect(url_for("main.index"))

    return render_template("add_task.html")


@main.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_task(id):
    task = Task.query.get_or_404(id)

    if request.method == "POST":
        task.title = request.form["title"]
        task.description = request.form.get("description", "")
        db.session.commit()

        return redirect(url_for("main.index"))

    return render_template("edit_task.html", task=task)


@main.route("/delete/<int:id>")
def delete_task(id):
    task = Task.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()

    return redirect(url_for("main.index"))

