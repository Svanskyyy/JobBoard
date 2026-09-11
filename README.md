# JobBoard

JobBoard is a Flask-based web application for publishing, browsing, searching, and managing job vacancies.

The project was developed as a final project for the Python with Flask & Django course.

## Live Demo

https://jobboard-fwnm.onrender.com/

## GitHub Repository

https://github.com/Svanskyyy/JobBoard

## Features

- User registration and login
- Secure password hashing
- User profile management
- Profile picture upload
- Create job vacancies
- View job details
- Edit and delete own vacancies
- Ownership-based authorization
- Job categories
- Search by job title, company, or description
- Filter by category and location
- Sort vacancies by newest or oldest
- Public author job pages
- My Jobs dashboard
- English and Georgian interface
- Custom 403, 404, and 500 error pages
- CSRF protection with Flask-WTF
- External NBG currency API integration
- USD and EUR salary conversion to GEL
- Application logging
- Automated tests with pytest
- PostgreSQL production database
- Responsive Bootstrap interface

## Technologies

- Python
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- Flask-Login
- Flask-WTF
- WTForms
- Jinja2
- PostgreSQL
- Psycopg
- Requests
- Pillow
- Pytest
- Bootstrap 5
- HTML
- CSS
- Gunicorn
- Git
- GitHub
- Render

## Project Structure

```text
JobBoard/
│
├── app/
│   ├── auth/
│   ├── errors/
│   ├── jobs/
│   ├── main/
│   ├── services/
│   ├── static/
│   ├── templates/
│   ├── __init__.py
│   ├── extensions.py
│   ├── logging_config.py
│   ├── models.py
│   └── translations.py
│
├── migrations/
├── tests/
├── .env.example
├── .gitignore
├── .python-version
├── config.py
├── requirements.txt
├── run.py
└── seed.py