from flask import Flask, render_template, Response

from modules.camera_module import VideoCameraModule

class CameraController:
    def __init__(self):
        self.camera = VideoCameraModule()

    def generate_frame(self):
        while True:
            frame = self.camera.get_frame()
            yield (b"--frame\r\n" b"Content-Type: image/jpeg\r\n\r\n" + frame + b"\r\n\r\n")

    def get_camera_stream(self):
        return Response(
            self.generate_frame(),
            mimetype="multipart/x-mixed-replace; boundary=frame",
        )
