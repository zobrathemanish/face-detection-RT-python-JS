import numpy as np
import argparse
import imutils
import time
import cv2
from imutils.video import FileVideoStream
from imutils.video import FPS

class VideoCamera(object):
    def __init__(self):
        # Using OpenCV to capture from device 0. If you have trouble capturing
        # from a webcam, comment the line below out and use a video file
        # instead.
        # self.video = cv2.VideoCapture(0)
        # If you decide to use video.mp4, you must have this file in the folder
        # as the main.py.
        self.video = FileVideoStream("cropvideo.mp4").start()
    
    def __del__(self):
        self.video.release()
    
    def get_frame(self):

        image = self.video.read()
        faceCascade = cv2.CascadeClassifier('haarcascade_profileface.xml')
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, 1.1, 4)

        # We are using Motion JPEG, but OpenCV defaults to capture raw images,
        # so we must encode it into JPEG in order to correctly display the
        # video stream.

        for (x, y, w, h) in faces:
        	cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()
