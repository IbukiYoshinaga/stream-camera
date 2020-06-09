from dotenv import load_dotenv
import os
from os.path import join, dirname
import uuid

from flask import Flask, render_template, Response

from controllers.camera_stream_controller import *

dotenv_path = join(dirname(__file__), '.env')

app = Flask(__name__)

camera_controller = CameraController()

class CameraInit():
    def __init__(self):
        #device_keyに関する初期設定
        load_dotenv(dotenv_path)
        app.run(host="0.0.0.0", debug=True)

    @app.route("/camera_stream")
    def generate_video():
        return camera_controller.get_camera_stream()


if __name__ == "__main__":
    CameraInit()