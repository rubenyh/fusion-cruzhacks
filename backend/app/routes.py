from fastapi import APIRouter, UploadFile, File, Form
from datetime import datetime
import cv2
import numpy as np
import os

from app.model import WasteDetector

router = APIRouter()
detector = WasteDetector()

os.makedirs("alerts", exist_ok=True)

@router.post("/predict")
async def predict(file: UploadFile = File(...)):
    contents = await file.read()

    nparr = np.frombuffer(contents, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    predictions = detector.predict(img)

    return predictions


@router.post("/alert")
async def alert( camera_id: str = Form(...), timestamp: str = Form(...), confidence: float = Form(...), image: UploadFile = File(...) ):
    contents = await image.read()

    filename = f"{camera_id}_{datetime.utcnow().timestamp()}.jpg"
    path = os.path.join("alerts", filename)

    with open(path, "wb") as f:
        f.write(contents)

    alert_data = {
        "camera_id": camera_id,
        "timestamp": timestamp,
        "confidence": confidence,
        "image_path": path
    }

    print("NEW TRASH ALERT:", alert_data)

    # here goes sms
    return {
        "status": "alert_received",
        "data": alert_data
    }
