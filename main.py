from typing import Optional
from fastapi import FastAPI
from todo import todo_router
from ex06_UploadFile.static.images.upload import upload_router

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}

@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}

@app.get("/users/{user_id}/name/{user_name}")
async def get_user(user_id: int, user_name: str):
    return {"message": f"user id: {user_id}, user name: {user_name}"}

@app.get("/query_test")
async def get_user(query: str):
    return {"message": f"query: {query}"}

@app.get("/sum")
async def sum(num1: int, num2: int):
    return {"sum": f"{num1} + {num2} = {num1 + num2}"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None):
    # typing.Union: Union[X, Y]는 X 또는 Y를 의미
    # typing.Optional: Optional[X]는 X 또는 None과 동일( or Union[X, None]과 동일)
    return {"item_id": item_id, "q": q}

app.include_router(todo_router)
app.include_router(upload_router)