from fastapi import FastAPI
from fastapi.middleware.wsgi import WSGIMiddleware
from flask import Flask

from ferialabs import settings

# Define Flask and FastAPI apps
fastapi_application = FastAPI()
flask_application = Flask(__name__)
flask_application.config.from_object(settings)

# Mount FastAPI with Flask in admin sub index
fastapi_application.mount("/admin", WSGIMiddleware(flask_application))

from ferialabs import db # noqa
from ferialabs import api  # noqa
from ferialabs import admin # noqa
