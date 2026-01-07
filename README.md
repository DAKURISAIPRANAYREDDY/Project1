**Project Overview and Purpose**

Project Title: Task Tracker
Purpose:
A web-based Task Tracker / To-Do management system that lets users add, view, update, and delete tasks.
This type of app is typically used to track daily work or personal tasks.

Key goals likely include:
1.Provide a simple UI for task management
2.Support CRUD (Create, Read, Update, Delete) operations
3.Store tasks persistently via a backend

**Technology Stack**
Layer	Technology
Backend:	Python, Flask
Frontend:	HTML5, CSS3
Database:	SQLite
API:	RESTful API (Flask)
Server:	Gunicorn
OS:	Linux
Version Control:	Git, GitHub

**System Architecture & Folder Structure**

Project1/
│
└── Task_Tracker/
    │
    ├── app/
    │   ├── __init__.py          # App factory and configuration
    │   ├── api.py               # API endpoints (if exposed)
    │   ├── models.py            # Database models
    │   ├── routes.py            # Application routes
    │   │
    │   ├── static/
    │   │   └── style.css        # Application styling
    │   │
    │   └── templates/
    │       ├── base.html        # Base layout
    │       ├── index.html       # Task list page
    │       ├── add_task.html    # Add task page
    │       └── edit_task.html   # Edit task page
    │
    ├── run.py                   # Application entry point
    ├── requirements.txt         # Project dependencies
    └── .gitignore               # Ignored files


**Architecture Flow**

run.py → starts the Flask server

__init__.py → initializes Flask app and database

models.py → defines Task table

routes.py → handles UI routes

api.py → handles API-based operations

Templates → render dynamic HTML pages

Static → handles CSS


** Installation and Setup Instructions**
1️⃣ Clone the Repository
git clone https://github.com/DAKURISAIPRANAYREDDY/Project1.git
cd Project1/Task_Tracker

2️⃣ Create Virtual Environment
python -m venv venv
source venv/bin/activate      # macOS / Linux
venv\Scripts\activate         # Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run the Application
python run.py

5️⃣ Open Browser
http://127.0.0.1:5000/


**Usage Guide**
Home Page (index.html)
1.Displays all tasks
2.Options to Edit or Delete tasks

Add Task
1.Navigate to add task page
2.Enter task details
3.Submit to save task

Edit Task
1.Modify existing task details
2.Save updates

Delete Task
1.Remove task permanently from database

**API Documentation**
| Endpoint          | Method | Description       |
| ----------------- | ------ | ----------------- |
| `/api/tasks`      | GET    | Get all tasks     |
| `/api/tasks`      | POST   | Create a new task |
| `/api/tasks/<id>` | PUT    | Update a task     |
| `/api/tasks/<id>` | DELETE | Delete a task     |

**
Testing Procedures**

Currently:
No automated tests implemented

Manual Testing
Run the application
Add tasks
Edit tasks
Delete tasks
Refresh page to confirm persistence


**Known Issues and Limitations**
No user authentication
No role-based access
Basic UI (not mobile responsive)
No form validation for incorrect input
No automated test coverage
SQLite is not suitable for large-scale production


**Future Enhancement Roadmap**

Add user login and authentication
Add task priority and deadlines
Add task status (completed / pending)
Improve UI with Bootstrap or Tailwind CSS
Add REST API documentation (Swagger)
Deploy to cloud (Render / Railway / AWS)
Add automated unit and integration tests

Contributor
DAKURISAIPRANAYREDDY

