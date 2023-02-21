import os
import dotenv
from pydantic import BaseSettings


dotenv.load_dotenv(dotenv_path=".env")
ENV_TYPE = os.environ.get("ENVIRONMENT")


class EnvironmentSettings(BaseSettings):
    SECRET_KEY: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


class DevelopmentSettings(EnvironmentSettings):
    pass


class ProductionSettings(EnvironmentSettings):
    pass


class LocalSettings(EnvironmentSettings):
    pass
