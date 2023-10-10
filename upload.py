from fastapi import APIRouter
from fastapi import File, UploadFile, HTTPException
from fastapi.responses import FileResponse
from pathlib import Path
import shutil
from ocr_test import detect_license_plate

upload_router = APIRouter()

@upload_router.get("/upload/")
async def upload_page():
    return FileResponse("templates/upload_page.html", media_type="text/html")

@upload_router.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    """
    file: 함수의 매개변수로 클라이언트로부터 전송된 파일을 받음.
    UploadFile: FastAPI에서 제공하는 클래스로 업로드된 파일의 정보와 내용을 담고 있다.
    File(...): FastAPI에서 제공하는 함수로 업로드된 파일을 받아올 수 있게 해줌.
    """
    ### 허용되지 않는 확장자의 파일이 업로드되면 400 상태 코드와 "Invalid file type" 메시지를 반환
    file_extension = Path(file.filename).suffix     # 파일의 확장자를 추출
    if file_extension not in ['.jpg', '.png', '.jpeg']:
        raise HTTPException(status_code=400, detail="Invalid file type")

    ### 파일 저장:
    # "uploaded_files"라는 디렉터리에 클라이언트로부터 받은 파일의 이름(file.filename)으로 파일을 바이너리 쓰기 모드("wb")로 연다.
    with open(Path("uploaded_files") / file.filename, "wb") as buffer:
        # shutil 모듈의 copyfileobj 함수를 사용하여 업로드된 파일의 내용(file.file)을 위에서 열린 파일(buffer)로 복사함.
        shutil.copyfileobj(file.file, buffer)

    file_path = Path("uploaded_files") / file.filename
    detect_license_plate(file_path)

    # 처리된 이미지 파일 반환
    return FileResponse("detected_image.jpg")
    # return {"filename": file.filename}  # 파일이 성공적으로 업로드되면, 업로드된 파일의 이름을 JSON 형태로 응답으로 반환

@upload_router.post("/detect_license/")
async def detect_plate():
    image_name = "35202747_001.jpg"
    file_path = Path("uploaded_files") / image_name
    if not file_path.exists() or not file_path.is_file():
        return {"error": "Image not found"}

    detect_license_plate(file_path)

    # 처리된 이미지 파일 반환
    return FileResponse("detected_image.jpg")

