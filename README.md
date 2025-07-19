# Snapshots Web App

A lightweight, Flask-based web application that captures live video using OpenCV, displays it in your browser, and allows you to take snapshots with a click.

---

## Features

- Live webcam stream via browser (MJPEG)
- Snapshot capture with a button
- Snapshots stored locally and viewable in-browser
- Clean, minimal architecture with Flask & OpenCV
- Easily extendable for object detection (e.g., weapons, intruders)

---

## Project Structure

```
smart_surveillance/
├── app.py               # Flask application
├── camera.py            # OpenCV webcam interface
├── templates/
│   └── index.html       # Live view & snapshot UI
├── static/
│   └── snapshots/       # Captured snapshot storage
└── README.md            # This file
```

---

## How It Works

1. `camera.py` uses OpenCV to capture frames from the webcam.
2. `app.py` runs a Flask server with endpoints:
   - `/` → UI page with live stream and snapshot button
   - `/video_feed` → MJPEG stream of camera feed
   - `/capture` → Captures and stores snapshot
3. Snapshots are saved under `static/snapshots/` and listed in the UI.

---

## Installation

### 1. Clone the repo

```bash
git clone https://github.com/your-username/smart_surveillance.git
cd smart_surveillance
```

### 2. Install dependencies

```bash
pip install flask opencv-python
```

---

## Usage

```bash
python app.py
```

Then visit:  
http://localhost:5000

---

## Captured Snapshots

All snapshots are saved to:

```
static/snapshots/
```

They are timestamped and displayed at the bottom of the UI.

---

## Future Extensions

You can easily extend this project to include:

- YOLOv8 or other object detection
- Email or Telegram alert system
- Zone-based motion detection
- Face/person recognition
- Intrusion or weapon detection

---

## License

This project is for educational purposes and can be reused with attribution.

---
