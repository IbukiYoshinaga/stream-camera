from flask import Flask, render_template, Response

import threading


class CameraController:
    def generate_frame(self, camera):
        while True:
            frame = camera.get_jpeg()
            yield (
                b"--frame\r\n" b"Content-Type: image/jpeg\r\n\r\n" + frame + b"\r\n\r\n"
            )

    def get_camera_stream(self, camera):
        return Response(
            self.generate_frame(camera),
            mimetype="multipart/x-mixed-replace; boundary=frame",
        )
