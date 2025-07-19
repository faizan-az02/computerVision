from flask import Flask, render_template, Response, redirect, url_for
from camera import VideoCamera
import os

app = Flask(__name__)
camera = VideoCamera()

@app.route('/')
def index():
    snapshots = os.listdir('static/snapshots')
    snapshots.sort(reverse=True)
    return render_template('index.html', snapshots=snapshots)


@app.route('/video_feed')
def video_feed():
    return Response(
        camera.stream(),
        mimetype='multipart/x-mixed-replace; boundary=frame'
    )

@app.route('/capture')
def capture():
    filename = camera.capture_frame()
    return redirect(url_for('index'))

if __name__ == '__main__':
    os.makedirs("static/snapshots", exist_ok=True)
    app.run(debug=True)
