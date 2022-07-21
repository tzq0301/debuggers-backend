from pydantic import BaseSettings


class Settings(BaseSettings):
    mysql_username: str
    mysql_password: str

    class Config:
        env_file = ".env"
