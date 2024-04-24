#!/bin/bash
# Requires the database to be up
FLASK_ENV=development DATABASE_URI="postgresql://myuser:mypassword@db/mydatabase" python manage.py
