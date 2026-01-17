from fastapi import APIRouter, UploadFile, File
import cv2
import numpy as np
from app.model import WasteDetector

router = APIRouter()
detector = WasteDetector()

@router.post("/predict")
async def predict(file: UploadFile = File(...)):

    contents = await file.read()

    nparr = np.frombuffer(contents, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    predictions = detector.predict(img)

    return predictions
