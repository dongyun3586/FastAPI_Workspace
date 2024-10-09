from typing import Union
from fastapi import FastAPI
from todo import todo_router
'''
fast api에서는 request body를 검사하기 위해 Pydantic models 를 사용한다
Request Body : 클라이언트가 서버로 데이터를 보낼 때 사용되는 데이터
'''
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


app.include_router(todo_router)

'''
http://127.0.0.1:8000/docs
'''