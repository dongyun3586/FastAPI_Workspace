from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

'''
https://fastapi.tiangolo.com/ko/#_4

[실습 1] 
http://127.0.0.1:8000/
{"Hello":"World"}

[실습 2]
http://127.0.0.1:8000/items/5
{"item_id":5,"q":null}

http://127.0.0.1:8000/items/5?q=somequery
{"item_id":5,"q":"somequery"}

[실습 3]
http://127.0.0.1:8000/docs
'''