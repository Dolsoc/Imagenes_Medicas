import os
import subprocess
import pydicom
from io import BytesIO
from app.config import ORTHANC_URL, ORTHANC_AE_TITLE, ORTHANC_PORT, ORTHANC_AUTH

DCMTK_PATH = "C:\\dcmtk-3.6.9-win64-dynamic\\bin\\storescu.exe"

def process_dicom(dicom_data: BytesIO):
    """
    Procesa el archivo DICOM recibido y lo envía a Orthanc usando DCMTK (storescu).
    """
    try:
        # Leer el archivo DICOM con PyDicom
        dicom_obj = pydicom.dcmread(dicom_data)

        # Convertir los datos a bytes
        dicom_bytes = dicom_data.getvalue()

        # Guardar temporalmente el archivo DICOM en el sistema de archivos
        dicom_file_path = "temp.dcm"
        with open(dicom_file_path, "wb") as f:
            f.write(dicom_bytes)

        # Ejecutar el comando storescu de DCMTK para enviar la imagen a Orthanc
        cmd = [
            DCMTK_PATH,
            "-aec", ORTHANC_AE_TITLE,  # AE Title de Orthanc
            "-aet", "MY_MODALITY",     # AE Title de nuestro dispositivo
            f"{ORTHANC_URL}:{ORTHANC_PORT}",
            dicom_file_path
        ]

        # Ejecutar el comando
        subprocess.run(cmd, check=True)

        # Eliminar el archivo temporal
        os.remove(dicom_file_path)

        return {"message": "Imagen DICOM subida a Orthanc correctamente."}
    except Exception as e:
        return {"error": f"Error al procesar el archivo DICOM: {str(e)}"}
