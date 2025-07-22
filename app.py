from flask import Flask, render_template, Response, redirect, url_for, jsonify
from camera import VideoCamera
import os

app = Flask(__name__)
camera = VideoCamera()

@app.route('/')
def index():

    snapshots = os.listdir('static/snapshots')
    # Filter out non-image files
    image_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp'}
    snapshots = [f for f in snapshots if any(f.lower().endswith(ext) for ext in image_extensions)]
    snapshots.sort(reverse=True)
    return render_template('index.html', snapshots=snapshots)

@app.route('/video_feed')
def video_feed():

    return Response(
        camera.stream(),
        mimetype='multipart/x-mixed-replace; boundary=frame'
    )

@app.route('/capture', methods=['POST', 'GET'])
def capture():
    
    filename = camera.capture_frame()
    return jsonify({'success': True, 'filename': filename})

@app.route('/check_snapshots')
def check_snapshots():
    snapshots = os.listdir('static/snapshots')
    # Filter out non-image files
    image_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp'}
    snapshots = [f for f in snapshots if any(f.lower().endswith(ext) for ext in image_extensions)]
    snapshots.sort(reverse=True)
    return jsonify({'snapshots': snapshots})

if __name__ == '__main__':
    os.makedirs("static/snapshots", exist_ok=True)
    app.run(debug=True)
