import os
import typing as t
import dotenv
from pydantic import BaseSettings


dotenv.load_dotenv(dotenv_path=".env")
ENV_TYPE = os.environ.get("ENVIRONMENT")


class EnvironmentSettings(BaseSettings):
    SECRET_KEY: str
    ENV_TYPE: str = ENV_TYPE
    DB_HOST: str = os.environ.get("DB_HOST")
    DB_PORT: str = os.environ.get("DB_PORT")
    DB_USER: str = os.environ.get("DB_USER")
    DB_NAME: str = os.environ.get("DB_NAME")
    DB_PASSWORD: str = os.environ.get("DB_PASSWORD")
    SQLALCHEMY_DATABASE_URI: str = (
        f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )
    _FLASK_BASIC_AUTH_USERNAME: str = os.environ.get("FLASK_BASIC_AUTH_USERNAME")
    _FLASK_BASIC_AUTH_PASSWORD: str = os.environ.get("FLASK_BASIC_AUTH_PASSWORD")
    ADMIN_BASIC_AUTH_USER: t.Dict[str, str] = {
        "username": _FLASK_BASIC_AUTH_USERNAME,
        "password": _FLASK_BASIC_AUTH_PASSWORD,
    }
    FLASK_ADMIN_SWATCH: str = "flatly"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


class DevelopmentSettings(EnvironmentSettings):
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


class ProductionSettings(EnvironmentSettings):
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


class LocalSettings(EnvironmentSettings):
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
