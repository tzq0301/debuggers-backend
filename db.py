import pymysql
from sqlalchemy import create_engine, Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config import get_settings

pymysql.install_as_MySQLdb()

settings = get_settings()

SQLALCHEMY_DATABASE_URL = f"""
    mysql://{settings.mysql_username}:{settings.mysql_password}@{settings.mysql_url}/{settings.mysql_database}
""".strip()

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class User(Base):
    __tablename__ = "user"

    username = Column(String, primary_key=True, index=True)
    password = Column(String, nullable=False)
