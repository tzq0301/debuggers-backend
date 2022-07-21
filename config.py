from functools import lru_cache

from pydantic import BaseSettings


@lru_cache()
def get_settings():
    return Settings()


class Settings(BaseSettings):
    mysql_username: str
    mysql_password: str
    mysql_url: str
    mysql_database: str

    class Config:
        env_file = ".env"
