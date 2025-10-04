from fastapi import APIRouter, File, UploadFile
from app.services import process_dicom
from io import BytesIO

router = APIRouter()

@router.post("/upload_dicom")
async def upload_dicom(file: UploadFile = File(...)):
    """
    Recibe un archivo DICOM, lo procesa y lo almacena para su recuperación.
    """
    try:
        # Leer el archivo recibido como bytes
        dicom_file = await file.read()

        # Convertir los bytes a un objeto DICOM
        dicom_data = BytesIO(dicom_file)
        
        # Aquí puedes procesar el archivo (por ejemplo, enviarlo a PACS o almacenarlo localmente)
        process_dicom(dicom_data)  # Función que procesará el archivo DICOM
        
        return {"message": "Imagen DICOM subida y procesada correctamente."}
    except Exception as e:
        return {"error": f"Error al subir la imagen DICOM: {str(e)}"}
