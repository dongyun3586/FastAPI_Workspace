from fastapi import FastAPI
from typing import Union, Optional
from todo import todo_router

app = FastAPI()

app.include_router(todo_router)