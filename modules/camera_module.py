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
        average = None
        threshold = 30
        min_distance = 1000
        while True:
            success, image = self.video.read()
            image = cv2.medianBlur(image, 5)
            gray_scale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            if average is None:
                average = gray_scale.copy().astype("float")
                continue
            cv2.accumulateWeighted(gray_scale, average, 0.6)

            frame_delta = cv2.absdiff(gray_scale, cv2.convertScaleAbs(average))
            frame_delta[frame_delta < threshold] = 0
            frame_delta[frame_delta >= threshold] = 255

            move_object = cv2.countNonZero(frame_delta)

            if move_object > min_distance:
                cv2.imwrite("move_object.jpg", frame_delta)

            cv2.imwrite("record.jpg", image)
            ret, jpeg = cv2.imencode(".jpg", image)
            self.jpeg = jpeg.tobytes()

    def get_jpeg(self):
        return self.jpeg
