from fastapi import APIRouter, UploadFile, File

router = APIRouter()

@router.post("/detect")
async def detect_health(file: UploadFile = File(...)):
    return {"status": "healthy"}