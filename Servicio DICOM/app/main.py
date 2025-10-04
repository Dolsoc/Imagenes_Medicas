from fastapi import FastAPI
from app.api.dicom_routes import router as dicom_router

app = FastAPI()

app.include_router(dicom_router)
