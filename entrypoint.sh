#!/bin/bash
# Update Database Migrations
alembic -c ferialabs/db/alembic.ini upgrade head
# Run Flask App with Gunicorn
uvicorn ferialabs.application:fastapi_application --proxy-headers --host 0.0.0.0 --port 80
