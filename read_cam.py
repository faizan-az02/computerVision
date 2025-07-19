import cv2
import os
from datetime import datetime

# Setup
output_dir = "snapshots"
os.makedirs(output_dir, exist_ok=True)

cap = cv2.VideoCapture(0)  # 0 = default webcam

print("[INFO] Press 's' to save a snapshot, 'q' to quit.")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow("Live Feed - Webcam", frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('s'):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = os.path.join(output_dir, f"snapshot_{timestamp}.jpg")
        cv2.imwrite(filename, frame)
        print(f"[SAVED] {filename}")
    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
