from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from uploadFile import uploade_router

app = FastAPI()

# /static 경로로 들어오는 요청에 대해 static 디렉토리의 정적 파일을 제공함.
app.mount("/static", StaticFiles(directory="static"))

@app.get("/")
async def root():
    return FileResponse("static/html/index.html", media_type="text/html")

@app.get("/hello")
async def hello():
    return {"message": "Hello World"}

app.include_router(uploade_router)