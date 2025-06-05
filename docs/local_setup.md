# Local Setup

This page provides a brief guide for setting up a development environment.

1. Ensure Python 3.11 or later is installed.
2. Create a virtual environment and install dependencies using `pip install -r requirements.txt`.
3. Run `python manage.py migrate` to create the SQLite database.
4. (Optional) Create a superuser to access the Django admin with `python manage.py createsuperuser`.
5. Start the development server via `python manage.py runserver`.

The default database is SQLite and is stored in `db.sqlite3`. Feel free to adjust the settings in `Reborn/settings.py` if you need a different database engine.

## Docker development

If you prefer using Docker, build and start the services with:

```bash
docker-compose up --build
```

This will run the development server on port 8000 and automatically apply database migrations.

