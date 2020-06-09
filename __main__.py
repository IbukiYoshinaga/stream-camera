from flask import Flask, render_template, Response

from controllers.camera_stream_controller import *

app = Flask(__name__)


@app.route("/camera_stream")
def generate_video():
    return start_camera_stream()


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
