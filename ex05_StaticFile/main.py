from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"))

@app.get("/")
async def root():
    return FileResponse("static/html/index.html", media_type="text/html")

@app.get("/hello")
async def hello():
    return {"message": "Hello World"}