import cv2
import numpy as np
from ultralytics import YOLO

class WasteDetector:
    def __init__(self, model_path: str = "models/ocean_waste.pt"):
        try:
            self.model = YOLO(model_path)
        except:
            self.model = None
            print("Model not loaded yet – using mock mode")

    def predict(self, image: np.ndarray):
        if self.model is None:
            return self.mock_prediction()

        results = self.model(image)
        return self.format_results(results)

    def mock_prediction(self):
        return {
            "objects": [
                {
                    "class": "plastic",
                    "confidence": 0.87,
                    "bbox": [100, 120, 200, 240]
                }
            ],
            "note": "MOCK DATA – real model not connected yet"
        }

    def format_results(self, results):
        detections = []

        for result in results:
            for box in result.boxes:
                detections.append({
                    "class": result.names[int(box.cls)],
                    "confidence": float(box.conf),
                    "bbox": box.xyxy.tolist()[0]
                })

        return {"objects": detections}
