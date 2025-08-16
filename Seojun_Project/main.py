from typing import Union
from fastapi import FastAPI

app = FastAPI()
req_status = False
time = 0


@app.get("/")
def root():
    return {"message": "Hi World"}


@app.get("/check")
def check():
    global req_status
    if req_status:
        req_status = False
        return f'<msg>{time}</msg>>'
    else:
        return ""


@app.get("/new")
def new_time(seconds):
    global time
    global req_status

    time = seconds
    req_status = True
    return f'Added {seconds} seconds.'