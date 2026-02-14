from flask import Flask, Response, render_template_string, request
import subprocess
import threading
import time
from functools import wraps

app = Flask(__name__)

# ---------------- HTML ----------------

HTML_PAGE = """
<!DOCTYPE html>
<html>
<body>
<h2>Live Video Stream</h2>

<img src="/video_feed">

<br><br>

<audio controls autoplay>
    <source src="/audio_feed" type="audio/wav">
    Your browser does not support audio.
</audio>

</body>
</html>
"""

# ---------------- Authentication ----------------

USERNAME = "dsc"
PASSWORD = "dscOK!@A310"

def check_auth(u, p):
    return u == USERNAME and p == PASSWORD

def authenticate():
    return Response(
        "Authentication required",
        401,
        {"WWW-Authenticate": 'Basic realm="Camera"'}
    )

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated

# ---------------- Video (threaded, shared) ----------------

latest_frame = None
frame_lock = threading.Lock()
'''
def camera_thread():
    global latest_frame

    cmd = [
        "libcamera-vid",
        "--inline",
        "--nopreview",
        "--codec", "mjpeg",
        "--width", "640",
        "--height", "480",
        "--framerate", "10",
        "-t", "0",
        "-o", "-"
    ]

    process = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
        bufsize=0
    )

    buffer = b""

    while True:
        buffer += process.stdout.read(4096)

        start = buffer.find(b'\xff\xd8')
        end = buffer.find(b'\xff\xd9')

        if start != -1 and end != -1:
            frame = buffer[start:end + 2]
            buffer = buffer[end + 2:]

            with frame_lock:
                latest_frame = frame
'''

def camera_thread():
    global latest_frame

    cmd = [
        "ffmpeg",
        "-f", "v4l2",
        "-input_format", "yuyv422",
        "-video_size", "320x240",
        "-framerate", "30",
        "-i", "/dev/video0",
        "-f", "mjpeg",
        "-q:v", "5",
        "-an",
        "-"
    ]

    process = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
        bufsize=0
    )

    buffer = b""

    while True:
        chunk = process.stdout.read(4096)
        if not chunk:
            continue

        buffer += chunk

        while True:
            start = buffer.find(b'\xff\xd8')
            end = buffer.find(b'\xff\xd9')

            if start != -1 and end != -1:
                frame = buffer[start:end + 2]
                buffer = buffer[end + 2:]

                with frame_lock:
                    latest_frame = frame
            else:
                break
            
def generate_frames():
    while True:
        with frame_lock:
            frame = latest_frame

        if frame:
            yield (
                b"--frame\r\n"
                b"Content-Type: image/jpeg\r\n\r\n"
                + frame +
                b"\r\n"
            )

        time.sleep(0.05)

# ---------------- Audio (PER CLIENT, NO THREADING) ----------------

@app.route("/audio_feed")
def audio_feed():

    def generate():
        cmd = [
            "ffmpeg",
            "-f", "alsa",
            "-ac", "4",
            "-ar", "16000",
            "-i", "hw:2,0",
            "-ac", "1",          # downmix to mono
            "-f", "wav",
            "-"
        ]

        with subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            bufsize=0
        ) as process:
            while True:
                data = process.stdout.read(4096)
                if not data:
                    break
                yield data

    return Response(generate(), mimetype="audio/wav")
# ---------------- Routes ----------------

@app.route("/")
def index():
    return render_template_string(HTML_PAGE)

@app.route("/video_feed")
@requires_auth
def video_feed():
    return Response(
        generate_frames(),
        mimetype="multipart/x-mixed-replace; boundary=frame"
    )

# ---------------- Main ----------------

if __name__ == "__main__":
    threading.Thread(target=camera_thread, daemon=True).start()
    app.run(host="0.0.0.0", port=5000, threaded=True)
