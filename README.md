# Career Mate (Team Eval)

A Django-based web application skeleton aimed at evaluating user skills and career interests. Currently, the repository serves as the foundation for a larger project, focusing primarily on customized user authentication and session management.

## Core Features & Architecture

- **Custom Authentication (`user` app)**: 
  - Implements a custom user model expanding the base Django `AbstractUser`.
  - Secure password hashing and robust sign-up/login/logout workflows.
  - Template-driven UI for authentication (Landing, Home, Signup, Login).
- **Skill Evaluation (`skill_eval` app)**: Bootstrapped Django application intended for implementing tests and tracking technical proficiencies. (WIP)
- **Interest Evaluation (`intrest_eval` app)**: Bootstrapped Django application meant for career interest matching and profiling. (WIP)

## Prerequisites

- **Python 3.10+**
- **Django 5.1+**
- **SQLite3** (Configured as default)

## Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone <repo-url>
   cd team_eval/career_mate
   ```
2. **Setup virtual environment**:
   ```bash
   python -m venv env
   source env/bin/activate
   # Note: A pre-existing 'env' folder is committed to the repo, it is recommended to create a fresh one for your architecture.
   ```
3. **Install Dependencies**:
   ```bash
   pip install django
   ```
4. **Run Database Migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

## Usage / Running Locally

To launch the development server, run:
```bash
python manage.py runserver
```

Navigate to `http://127.0.0.1:8000/` to access the landing page.

## Project Structure

```text
.
├── career_mate/           # Main project directory (settings, urls)
├── user/                  # Custom authentication application
│   ├── views.py           # Login/Signup routing
│   └── models.py          # Custom User definition
├── skill_eval/            # Application for technical assessments (scaffold)
├── intrest_eval/          # Application for career interest matching (scaffold)
├── templates/             # HTML files (landing.html, login.html, etc.)
├── static/                # CSS/JS Assets
└── manage.py              # Django execution entry point
```
