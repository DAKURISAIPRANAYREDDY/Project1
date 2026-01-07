from flask import Blueprint, jsonify, request

from .models import Task
from . import db

api_bp = Blueprint("api", __name__)


@api_bp.route("/tasks", methods=["GET"])
def get_tasks():
    tasks = Task.query.all()
    return jsonify([
        {
            "id": t.id,
            "title": t.title,
            "description": t.description,
            "done": t.done
        }
        for t in tasks
    ])


@api_bp.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json()
    task = Task(
        title=data["title"],
        description=data.get("description", "")
    )
    db.session.add(task)
    db.session.commit()
    return jsonify({"message": "Task created"}), 201


@api_bp.route("/tasks/<int:id>", methods=["PUT"])
def update_task(id):
    task = Task.query.get_or_404(id)
    data = request.get_json()

    task.title = data.get("title", task.title)
    task.description = data.get("description", task.description)
    task.done = data.get("done", task.done)

    db.session.commit()
    return jsonify({"message": "Task updated"})


@api_bp.route("/tasks/<int:id>", methods=["DELETE"])
def delete_task_api(id):
    task = Task.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    return jsonify({"message": "Task deleted"})
