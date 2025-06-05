# Reborn Community Control Center

This repository contains a small Django project used for managing the Reborn community members and servers. It exposes a basic website and XML feed that can be consumed by games like Arma.

## Features

- Django 4 based project.
- Admin interface provided by [django-grappelli](https://github.com/sehmaschine/django-grappelli).
- Displays a list of members grouped by rank.
- Provides an XML endpoint and binary logo file for use in third‑party tools.
- Comes with a basic test suite.

## Requirements

- Python 3.11+
- Django 4.2
- django-grappelli 3.x

All required Python packages are listed in [requirements.txt](requirements.txt).

## Installation

1. Create and activate a virtual environment (recommended):

   ```bash
   python3 -m venv env
   source env/bin/activate
   ```

2. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run migrations to set up the database:

   ```bash
   python manage.py migrate
   ```

## Running the development server

Execute the following command and open <http://localhost:8000/squad/> in a browser:

```bash
python manage.py runserver
```

The admin interface is available at `/admin/`.

## Running tests

The project includes a small test suite located in `squad/tests.py`. Run the tests with:

```bash
python manage.py test
```

## Project layout

```
├── Reborn/              # Project settings and URL configuration
├── squad/               # Application with models, views and tests
├── static/              # CSS and logo assets
├── templates/           # HTML and XML templates
└── manage.py            # Django management script
```

For additional details on configuring the project, see [docs/local_setup.md](docs/local_setup.md).

