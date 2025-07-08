from flask import Flask, render_template, Response, request
from application.models.face_recognition import face_detection
import time
import threading

video_frame = None
lock = threading.Lock()

app = Flask(__name__, template_folder = "application/templates")

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/upload')
def upload():
    global video_frame, lock
    
    image_data = request.data()

    with lock:
        global video_frame
        video_frame = image_data

    return "Gambar Diterima", 200

def generate_frame():
    global video_frame, lock
    while True:
        with lock:
            if video_frame is None:
                time.sleep(0.1)
                continue
            frame_copy = video_frame
        yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + frame_copy + b'\r\n')

@app.route('/video')
def video():
    return Response(generate_frame(), mimetype='multipart/x-mixed-replace; boundary:frame')

if __name__ == "__main__":
    app.run(debug=False, host = '0.0.0.0' , port = 4000)
