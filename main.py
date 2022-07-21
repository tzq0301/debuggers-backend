from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import db
from model import LoginInfo

app: FastAPI = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/login")
async def login(login_info: LoginInfo):
    return login_info
