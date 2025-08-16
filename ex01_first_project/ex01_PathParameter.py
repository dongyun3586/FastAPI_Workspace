from fastapi import FastAPI

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

'''
**`http://127.0.0.1:8000/users/me`**

**`http://127.0.0.1:8000/users/111`**

**`http://127.0.0.1:8000/users/111/name/Harry`**

⇒ *경로 동작*은 순차적으로 평가되기 때문에 `/users/{user_id}` 이전에 `/users/me`를 먼저 선언해야 한다.
'''