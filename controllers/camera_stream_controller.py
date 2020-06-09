from flask import Flask, render_template, Response

from modules.camera_module import VideoCameraClass


def generate_frame(camera):
    while True:
        frame = camera.get_frame()
        yield (b"--frame\r\n" b"Content-Type: image/jpeg\r\n\r\n" + frame + b"\r\n\r\n")


def start_camera_stream():
    return Response(
        generate_frame(VideoCameraClass()),
        mimetype="multipart/x-mixed-replace; boundary=frame",
    )
