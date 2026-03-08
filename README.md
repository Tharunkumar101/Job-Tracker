# 🗂️ Job Application Tracker

A web application to help job seekers track their job applications in one place.
Easily manage where you applied, what role, current status, and notes — all in a clean dashboard.

## 🛠️ Tech Stack
- **Django** — Frontend & Templates
- **FastAPI** — Backend REST API
- **PostgreSQL** — Database
- **Bootstrap 5** — UI Styling

## ✨ What You Can Do
- ➕ Add new job applications
- ✏️ Edit existing applications
- 🗑️ Delete applications
- 📊 View stats — Total, Interviews, Offers, Rejected
- 🔍 Search by company or role
- 🎯 Filter by status

## 🌐 API (FastAPI)
Run FastAPI on port 8001 to access all job data via REST API.
Visit `http://127.0.0.1:8001/docs` for interactive API docs.

## ⚙️ How to Run
```bash
# Clone the project
git clone https://github.com/Tharunkumar101/Job-Tracker.git

# Install dependencies
pip install -r requirements.txt

# Run Django
python manage.py runserver

# Run FastAPI
uvicorn fastapi_service.main:app --reload --port 8001
```

## 👨‍💻 Author
**Tharunkumar101** — Built this to manage job hunting smarter 🚀