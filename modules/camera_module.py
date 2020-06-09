# -*- coding: utf-8 -*-
import cv2
from os.path import join, dirname

# カメラ設定
class VideoCameraModule:
    def __init__(self):
        self.video = cv2.VideoCapture(0)

    def __del__(self):
        self.video.release()

    def get_frame(self):
        success, image = self.video.read()
        ret, jpeg = cv2.imencode(".jpg", image)
        #cv2.imwrite("test.jpg", jpeg)
        return jpeg.tobytes()
