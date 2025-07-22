import cv2
from datetime import datetime
import os
from ultralytics import YOLO
import requests

class VideoCamera:
    
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.model = YOLO('yolov8n.pt')  # Make sure yolov8n.pt is in the directory or provide the correct path

    def __del__(self):
        self.cap.release()

    def get_frame(self):
        ret, frame = self.cap.read()
        if not ret:
            return None
        
        # Run YOLOv8 detection
        results = self.model(frame, verbose=False)[0]

        # Draw bounding boxes and labels
        for box in results.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            cls = int(box.cls[0])
            label = self.model.names[cls]
            conf = float(box.conf[0])
            
            cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 255, 0), 2)
            cv2.putText(frame, f'{label} {conf:.2f}', (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 0), 2)
            
        if label == 'cell phone':
            requests.post('http://127.0.0.1:5000/capture')
        
        _, jpeg = cv2.imencode('.jpg', frame)
        return jpeg.tobytes()

    def stream(self):
        while True:
            frame = self.get_frame()
            if frame:
                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

    def capture_frame(self):
        ret, frame = self.cap.read()
        if ret:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"static/snapshots/snap_{timestamp}.jpg"
            cv2.imwrite(filename, frame)
            return filename
        return None
