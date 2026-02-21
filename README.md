# SDA Python Developer From Scratch

![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![License](https://img.shields.io/badge/license-MIT-blue)
![Python](https://img.shields.io/badge/python-3.14-blue)
![Django](https://img.shields.io/badge/django-6.x-green)
![Python](https://img.shields.io/badge/HTML-5-orange)
![Python](https://img.shields.io/badge/CSS-3-purple)
![Python](https://img.shields.io/badge/JavaScript-Vanilla-yellow)
![pytest](https://img.shields.io/badge/tested%20with-pytest-yellow)
![Status](https://img.shields.io/badge/status-%20completed-brightgreen)

This repository contains all the code I wrote during the **Python Developer From Scratch** bootcamp at [Software Development Academy Romania](https://sdacademy.ro/lista-de-cursuri/python/). It covers everything from Python fundamentals to full-stack web development with Django, across 280 hours of live, instructor-led sessions.

---

## Table of Contents

- [About](#about)
- [Certificate of Completion](#certificate-of-completion)
- [What I Learned](#what-i-learned)
- [Tech Stack](#tech-stack)
- [Repository Structure](#repository-structure)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Running the Django Project](#running-the-django-project)
- [Environment Variables](#environment-variables)
- [Running Tests](#running-tests)
- [Project Structure](#project-structure)
- [About the Bootcamp](#about-the-bootcamp)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## About

This is a personal learning repository. It documents my progress through a structured Python bootcamp that covers backend development, databases, testing, algorithms, design patterns, and frontend basics.

Every folder corresponds to a module from the course curriculum. The code here ranges from introductory exercises to a working Django web application with authentication, models, views, and templates.

---

## Certificate of Completion

![Certificate of Completion](https://)

---

## What I Learned

**Python Basics**
Core syntax, data types, control flow, functions, OOP (classes, inheritance, polymorphism, encapsulation, abstraction), file handling, modules, and packages.

**Python Technology**
Virtual environments, pip, package creation, built-in modules, and development tooling with PyCharm and VS Code.

**Python Intermediate**
Lambda expressions, decorators, iterators and generators, context managers, regular expressions, exception handling, multithreading, multiprocessing, serialization (JSON, CSV, Pickle), and profiling.

**GIT and Command Line**
Version control with Git: init, add, commit, branch, merge, rebase, and working with remote repositories on GitHub.

**Software Testing and TDD**
Unit testing with pytest, Test-Driven Development (TDD), fixtures, parametrize, coverage reports, and writing testable code.

**Algorithms and Data Structures**
Computational complexity (Big O), recursion, dynamic programming, sorting algorithms (Bubble Sort, Heap Sort, Quick Sort), stacks, queues, trees, graphs, and heaps.

**Design Patterns and Good Practices**
Creational patterns (Singleton, Factory Method, Abstract Factory, Builder, Prototype), structural patterns (Adapter, Decorator, Facade, Proxy, Bridge, Composite, Flyweight), behavioral patterns (Observer, Strategy, Command, State, Iterator, and more). Clean Code, SOLID, DRY, KISS, YAGNI.

**SQL Databases with MySQL**
Relational databases, DDL and DML, CRUD operations, JOINs, transactions, ACID principles, triggers, and stored procedures.

**Databases in Python**
Connecting to MySQL with Python, ORM with SQLAlchemy, working with SQLite, and database-driven application development.

**Introduction to HTTP**
HTTP methods, status codes, request/response cycle, REST principles, and how browsers and servers communicate.

**Front-End Development (Basics)**
HTML5, CSS3, Vanilla JavaScript, DOM manipulation, event handling, forms, and basic XHR requests.

**Backend Development with Django**
Django project and app structure, models, views, URLs, templates, forms, authentication, sessions, static files, migrations, Django Admin, and deployment basics.

---

## Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.14 |
| Backend Framework | Django 6.x |
| Database (development) | SQLite3 |
| Database (production) | MySQL 8.0 |
| ORM | Django ORM, SQLAlchemy |
| Testing | pytest, pytest-cov, UnitTest |
| Frontend | HTML5, CSS3, Vanilla JavaScript, Bootstrap |
| Version Control | Git, GitHub |
| IDE | PyCharm, VS Code |
| Environment | virtualenv, python-dotenv |

---

## Repository Structure

```
sda_python_developer_from_scratch/
|
+-- python_basics/                   # Core Python syntax, OOP, functions, data structures
+-- python_technology/               # Virtualenv, pip, packages, tooling
+-- python_intermediate/             # Decorators, generators, threading, regex, exceptions
+-- software_testing_and_tdd/        # pytest, TDD exercises, fixtures
+-- algorithms_and_data_structures/  # Sorting, trees, graphs, complexity
+-- design_patterns_and_good_practices/
|   +-- creational_patterns/
|   +-- structural_patterns/
|   +-- behavioral_patterns/
+-- databases_in_python/             # MySQL + Python, SQLAlchemy
+-- html_css_js/                     # Frontend exercises: HTML5, CSS3, JS
+-- backend_technology/              # Django project: movies watchlist app
+-- final_project/                   # Django final project: multi-app structure
+-- .env.example                     # Template for environment variables
+-- .gitignore
+-- requirements.txt
+-- README.md
```

---

## Getting Started

### Prerequisites

Make sure you have the following installed:

- Python 3.11 or higher
- pip
- Git
- MySQL 8.0 (only if you want to use the MySQL-based exercises)
- A virtual environment tool (`venv` is included with Python)

### Installation

1. Clone the repository:

```bash
git clone https://github.com/AndreiIliescu/sda_python_developer_from_scratch.git
cd sda_python_developer_from_scratch
```

2. Create and activate a virtual environment:

```bash
python -m venv .venv

# macOS / Linux
source venv/bin/activate

# Windows - CMD
.\.venv\Scripts\activate

# Windows - PowerShell
.\.venv\Scripts\activate.ps1
```

3. Install all dependencies:

```bash
pip install -r requirements.txt
```

4. Copy the environment variables template and fill in your values:

```bash
cp .env.example .env
```

---

## Running the Django Project

The main Django project lives in `backend_technology/` and the final project in `final_project/`.

Navigate to the project folder:

```bash
cd backend_technology
```

Apply migrations:

```bash
python.exe .\manage.py migrate
```

Create a superuser for Django Admin:

```bash
python.exe .\manage.py createsuperuser
```

Collect static files:

```bash
python.exe .\manage.py collectstatic
```

Start the development server:

```bash
python.exe .\manage.py runserver
```

Open your browser at `http://127.0.0.1:8000/`.

---

## Environment Variables

Create a `.env` file in the root of each Django project folder. Use `.env.example` as your starting point.

```env
SECRET_KEY=your_django_secret_key_here
DEBUG=True

# SQLite (development, default)
DB_ENGINE=django.db.backends.sqlite3
DB_NAME=db.sqlite3

# MySQL (production)
# DB_ENGINE=django.db.backends.mysql
# DB_NAME=your_database_name
# DB_USER=your_database_user
# DB_PASSWORD=your_database_password
# DB_HOST=localhost
# DB_PORT=3306

# PostgreSQL (alternative production option)
# DB_ENGINE=django.db.backends.postgresql
# DB_NAME=your_database_name
# DB_USER=your_database_user
# DB_PASSWORD=your_database_password
# DB_HOST=localhost
# DB_PORT=5432

ALLOWED_HOSTS=127.0.0.1,localhost
```

Never commit your actual `.env` file. The `.env.example` file in this repository contains only placeholder values.

---

## Running Tests

From the root of the repository, run all tests with:

```bash
pytest
```

Run tests for a specific module:

```bash
pytest software_testing_and_tdd/
```

Run with coverage report:

```bash
pytest --cov=. --cov-report=term-missing
```

Generate an HTML coverage report:

```bash
pytest --cov=. --cov-report=html
```

Then open `htmlcov/index.html` in your browser.

---

## Project Structure

Each module folder follows a consistent structure:

```
module_name/
+-- curs/           # Code written during class sessions
+-- exercitii/      # Exercises completed during class
+-- homework/       # Individual homework assignments
+-- tests/          # Test files for the module (where applicable)
```

The Django projects follow the standard Django layout:

```
backend_technology/
+-- movies/                  # Django project configuration
|   +-- settings.py
|   +-- urls.py
|   +-- wsgi.py
|   +-- asgi.py
+-- viewer/                  # Django application
|   +-- models.py
|   +-- views.py
|   +-- forms.py
|   +-- admin.py
|   +-- urls.py
|   +-- migrations/
|   +-- templates/
+-- static/
|   +-- css/
|   +-- images/
+-- manage.py
+-- .env.example
```

---

## About the Bootcamp

This repository documents work completed during the **Python Developer From Scratch** program at [Software Development Academy Romania](https://sdacademy.ro/lista-de-cursuri/python/).

| Detail | Info |
|---|---|
| Duration | 280 hours |
| Format | Online, live sessions, evenings |
| Certification | Accredited by the Romanian Ministry of Education and Ministry of Labor |
| Trainer | Ionut-Cristian Iordache, Senior Software Automation Developer at Grant Thornton Romania |
| Focus | Full-stack Python development, from basics to production-ready Django applications |

The curriculum covers 14 modules, from Python fundamentals to a final team project built following Scrum methodology.

---

## Contributing

This repository is personal coursework. It is not open for contributions. If you are following the same course and have questions, feel free to reach out via the contact details below.

---

## License

Distributed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contact

**Iliescu Andrei**

[![Email Outlook](https://img.shields.io/badge/Outlook-andrei.iliescu13102000%40outlook.com-0078D4?style=for-the-badge&logo=microsoftoutlook&logoColor=white)](mailto:andrei.iliescu13102000@outlook.com)

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Andrei_Iliescu-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/andrei-iliescu-aa7910214)

[![GitHub](https://img.shields.io/badge/GitHub-Andrei_Iliescu-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/AndreiIliescu)