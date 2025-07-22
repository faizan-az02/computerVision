# Snapshots Web App

A lightweight, Flask-based web application that captures live video using OpenCV, displays it in your browser, has YOLOv8 applied for detection of the objects, capture snapshots of specific ones and also allows you to take snapshots with a click.
The app also detects a sudden blackout (due to any tempering being done with the camera), snapshots it and shows it on the UI.

---

## Features

- Live webcam stream via browser (MJPEG)
- Object Detection with YOLOv8
- Detects sudden blackouts
- Capture snapshots for a specific object
- Snapshot capture with a button
- Snapshots stored locally and viewable in-browser
- Clean, minimal architecture with Flask & OpenCV
- Easily extendable for object detection (e.g., weapons, intruders)

---

## How It Works

1. `camera.py` uses OpenCV to capture frames from the webcam, is home for YOLOv8 Model, and detection logic.
2. `app.py` runs a Flask server with endpoints:
   - `/` → UI page with live stream and snapshot button
   - `/video_feed` → MJPEG stream of camera feed
   - `/capture` → Captures and stores snapshot
3. Snapshots are saved under `static/snapshots/` and listed in the UI.
4. In the current logic, app detects "cellphone" label, captures that frame. You can change it in the camera.py, where the detection "IF" is placed.
5. The gallery loads new image after 3 seconds using the polling logic, and also when the image is captured manually.
---

## Usage

Run:<br>
python app.py

Then visit:  
http://localhost:5000

## Captured Snapshots

All snapshots are saved to:

static/snapshots/

They are timestamped and displayed at the bottom of the UI.

## Future Extensions

You can easily extend this project to include:

- Email or Telegram alert system
- Zone-based motion detection
- Face/person recognition
- Intrusion or weapon detection

---

## License

This project is for educational purposes and can be reused with attribution.

---
