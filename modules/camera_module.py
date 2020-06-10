# -*- coding: utf-8 -*-
import cv2
from os.path import join, dirname

import threading

# カメラ設定
class VideoCameraModule:
    def __init__(self):
        self.video = cv2.VideoCapture(0)

    def __del__(self):
        self.video.release()

    def get_frame(self):
        while True:
            success, image = self.video.read()
            ret, jpeg = cv2.imencode(".jpg", image)
            self.jpeg = jpeg.tobytes()
            cv2.imwrite("test.jpg", image)

    def get_jpeg(self):
        return self.jpeg