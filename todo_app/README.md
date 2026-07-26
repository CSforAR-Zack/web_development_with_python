# Todo App

A simple Flask to-do list app built as a teaching example for a web development
with Python course. It demonstrates the Flask application factory pattern,
blueprints, SQLAlchemy models, Flask-Login authentication, and Flask-WTF forms.

## Features

- User accounts (create account, log in, log out)
- Create, edit, complete, and delete tasks
- Soft-deleted tasks view
- CSRF-protected forms

## Requirements

- Python 3.10+

## Setup

1. Create and activate a virtual environment:

   ```
   python -m venv .venv
   .venv\Scripts\activate
   ```

2. Install dependencies:

   ```
   pip install -r requirements.txt
   ```

3. Initialize the database (creates `instance/todo.db` and an `admin`/`pass` user):

   ```
   python init_db.py
   ```

4. Run the app:

   ```
   flask --app todo run --debug
   ```

   Then open http://127.0.0.1:5000 in your browser.

## Project Structure

```
todo/
├── __init__.py       # App factory
├── routes.py         # Routes (views)
├── forms.py          # Flask-WTF forms
├── models.py         # SQLAlchemy models
├── services.py       # Database/business logic
├── extensions.py     # Flask extensions (db, csrf, login manager)
├── static/           # CSS, JS, images
└── templates/         # Jinja templates
```

## Note

This project is for demonstration/teaching purposes. The secret key and
default credentials are not safe for production use.
