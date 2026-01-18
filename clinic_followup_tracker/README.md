# Clinic Follow-up Tracker (Django + MySQL)

## Project Overview
This project is a Django-based Clinic Follow-up Tracking System developed as part of an assignment.
It allows clinic staff to manage patient follow-ups, track their status, and share follow-up
information with patients using a secure public link.

The application uses MySQL as the backend database and follows Django best practices such as
authentication, ORM usage, and modular app structure.

---

## Features
- User authentication (Login / Logout)
- Admin panel for managing clinics, users, and follow-ups
- Clinic-based data isolation (each user sees only their clinic data)
- Dashboard with follow-up statistics (Total / Pending / Done)
- Create, edit, and mark follow-ups as done
- Secure public follow-up page using unique token (no login required)
- Public link view tracking (timestamp and IP address logging)
- View count displayed on dashboard
- CSV import of follow-ups using Django management command
- MySQL database integration

---

## Tech Stack
- Python 3.11
- Django 5.x
- MySQL 8.x
- HTML (Django Templates)

---

## Database Details
- MySQL is used as the primary database
- Django ORM is used for all database operations
- Database tables are created using Django migrations
- Main models include:
  - Clinic
  - UserProfile
  - FollowUp
  - PublicViewLog

---

## Project Structure
- core/
  - models.py
  - views.py
  - forms.py
  - admin.py
  - management/commands/import_followups.py
- config/
  - settings.py
  - urls.py
- templates/
  - dashboard.html
  - create_followup.html
  - edit_followup.html
  - public_followup.html
  - registration/login.html

---

## Public Follow-up Feature
Each follow-up generates a unique public token.
This token is used to create a public URL that can be shared with patients via SMS, WhatsApp, or email.

The public page:
- Does not require login
- Displays follow-up details
- Supports language-based messaging
- Logs every visit with timestamp and IP address

This helps clinic staff track whether a patient has viewed the follow-up.

---
## Setup and Run Instructions

### 1. Clone the Repository
git clone https://github.com/vamshialle66/clinic-followup-tracker.git
cd clinic-followup-tracker


### 2. Create and Activate Virtual Environment
python -m venv venv


**Activate the virtual environment:**

- Windows:
venv\Scripts\activate


- Linux / macOS:
source venv/bin/activate


### 3. Install Dependencies
pip install -r requirements.txt


### 4. Configure MySQL Database
Edit `config/settings.py` and update the database configuration:

DATABASES = {
'default': {
'ENGINE': 'django.db.backends.mysql',
'NAME': 'clinic_tracker',
'USER': 'root',
'PASSWORD': 'your_password',
'HOST': 'localhost',
'PORT': '3306',
}
}


Make sure MySQL server is running.

### 5. Run Database Migrations
python manage.py makemigrations
python manage.py migrate

### 6. Create Superuser
python manage.py createsuperuser


### 7. Start the Development Server
python manage.py runserver


### 8. Access the Application
- Admin Panel: http://127.0.0.1:8000/admin/
- Login Page: http://127.0.0.1:8000/accounts/login/
- Dashboard: http://127.0.0.1:8000/





## CSV Import Feature
The application supports bulk import of follow-ups using a CSV file.

Command to import:
python manage.py import_followups <csv_file> <clinic_id> <user_id>

CSV format:

---

## How to Run the Project
1. Create and activate a virtual environment
2. Install required Python dependencies
3. Configure MySQL database settings in `settings.py`
4. Run Django migrations
5. Start the Django development server
6. Access the application via browser

---



