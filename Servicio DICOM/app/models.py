from pydantic import BaseModel

class DicomFile(BaseModel):
    patient_name: str
    study_id: str
    modality: str