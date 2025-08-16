from fastapi import FastAPI
from typing import Union, Optional

app = FastAPI()


@app.get("/test")
async def get_user(query: str):
    return {"message": f"query: {query}"}


@app.get("/sum")
async def sum(a: int = 1, b: int = 10):
    s = 0
    for i in range(a, b+1):
        s += i
    return {"sum": s}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
'''
http://127.0.0.1:8000/test?query=hello
{"message":"query: hello"}

http://127.0.0.1:8000/sum?a=1&b=100
{"sum":5050}

Optional Parameter: 생략 가능한 query 파라미터를 만들고 싶은 경우 파이썬의 None을 이용하면 된다
http://127.0.0.1:8000/items/5
{"item_id":5,"q":null}

http://127.0.0.1:8000/items/5?q=somequery
{"item_id":5,"q":"somequery"}
'''