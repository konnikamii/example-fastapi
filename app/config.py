from logging import config
from pydantic_settings import BaseSettings
from pydantic.dataclasses import dataclasses
from pydantic import ConfigDict, BaseModel


# @dataclasses(config=ConfigDict(env_file="1apiLocal.env"))
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
