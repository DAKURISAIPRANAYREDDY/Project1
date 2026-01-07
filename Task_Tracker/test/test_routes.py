import os
import sys

import pytest

# Add Task_Tracker to PYTHONPATH
sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
)

from app import create_app, db


@pytest.fixture
def client():
    app = create_app(testing=True)
    app.config["TESTING"] = True

    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client


def test_create_task(client):
    response = client.post(
        "/api/tasks",
        json={
            "title": "Test Task",
            "description": "Testing create",
        },
    )

    assert response.status_code == 201
    assert response.get_json()["message"] == "Task created"


def test_get_tasks(client):
    client.post("/api/tasks", json={"title": "Task 1"})

    response = client.get("/api/tasks")
    data = response.get_json()

    assert response.status_code == 200
    assert len(data) == 1
    assert data[0]["title"] == "Task 1"




