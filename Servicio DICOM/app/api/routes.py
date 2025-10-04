from fastapi import APIRouter
from app.services import send_to_pacs

router = APIRouter()

@router.post("/upload_dicom")
async def upload_dicom(dicom_file: bytes):
    send_to_pacs(dicom_file)
    return {"message": "Imagen DICOM subida correctamente"}
