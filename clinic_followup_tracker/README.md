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



