from pydantic import ConfigDict, Field, BaseConfig
from pydantic_settings import BaseSettings, SettingsConfigDict

from typing import Annotated, TypeVar


class Settings(BaseSettings):
    database_hostname: str
    database_port: str
    database_password: str
    database_name: str
    database_username: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int
    model_config = {
        'env_file': "1apiLocal.env"
    }


settings = Settings()
