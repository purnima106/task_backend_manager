###🚀 **Task Manager Backend (Flask)**

A **production-grade Flask backend** for task management, featuring **AI-powered priority analysis (mock)**, **daily summary emails**, **logging**, and **pytest-based testing**.

## ✨ **Features**
- **✅ Task CRUD APIs** – Create, fetch, update, and delete tasks.
- **🤖 AI Priority Analysis** – Mocked AI logic (easily swappable with real OpenAI).
- **📧 Daily Summary Emails** – Automated reports with Flask-Mail + APScheduler.
- **📊 Task Summary Endpoint** – Displays pending, completed, and overdue tasks.
- **📝 Centralized Logging** – Rotating logs saved to `logs/app.log`.
- **🧪 Test Suite** – Pytest unit and API tests.
- **⚙️ Environment Config** – Uses `.env` for DB, email, and API keys.
- **🏗 MVC Architecture** – Controllers, Services, Models, Utils.

---

## 📂 **Project Structure**

task_manager_backend_prod/
│
├── app/
│   ├── controllers/       # API routes (tasks, summary)
│   ├── models/            # Database models
│   ├── services/          # AI, Email, and Task services
│   ├── scheduler/         # Email scheduling jobs
│   ├── utils/             # Helper functions & logging
│   ├── extensions.py      # Flask extensions
│   ├── config.py          # App configurations
│   └── __init__.py        # App factory
│
├── tests/                 # Pytest test cases
├── logs/                  # Application logs
├── requirements.txt       # Dependencies
├── README.md              # Documentation
└── wsgi.py                # App entry point

⚡ Quick Start
1. Clone the Repo
git clone https://github.com/<your-username>/task_manager_backend_prod.git
cd task_manager_backend_prod
2. Setup Virtual Environment
python -m venv .venv
source .venv/Scripts/activate   # Windows
3. Install Dependencies
pip install -r requirements.txt
4. Create .env File
MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASSWORD=your_mysql_password
MYSQL_DB=task_manager

MAIL_USERNAME=your_email@gmail.com
MAIL_PASSWORD=your_gmail_app_password
📡 API Endpoints
Tasks

POST /tasks/ – Create a task

json:

{ "title": "Test Task", "description": "Demo task" }
GET /tasks/ – Fetch all tasks

GET /tasks/<id> – Fetch a task by ID

PUT /tasks/<id> – Update a task

DELETE /tasks/<id> – Delete a task

Summary

GET /summary/ – Shows total tasks, completed, pending, overdue, and average urgency.

🧪 Testing
Run all tests:

bash
Copy
Edit
python -m pytest -v
📝 Logging
All logs are saved in logs/app.log.

Uses RotatingFileHandler for log rotation.

🚀 Future Enhancements
JWT-based authentication for APIs.

Real AI integration (OpenAI GPT models).

Task search, filters, and pagination.

Marshmallow schemas for request validation.

Author: Purnima Nahata
