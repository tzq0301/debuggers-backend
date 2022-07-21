import sqlalchemy.exc
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from db import User, get_db
from model import LoginInfo, RegisterInfo

app: FastAPI = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/login")
async def login(login_info: LoginInfo, db: Session = Depends(get_db)) -> bool:
    return db.query(User).filter(User.username == login_info.username).filter(
        User.password == login_info.password).one_or_none() is not None


@app.post("/register")
async def register(register_info: RegisterInfo, db: Session = Depends(get_db)) -> bool:
    user = User()
    user.username = register_info.username
    user.password = register_info.password
    db.add(user)
    try:
        db.commit()
    except sqlalchemy.exc.IntegrityError:
        return False
    return True
