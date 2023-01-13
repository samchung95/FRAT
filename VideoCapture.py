import cv2
import threading

class VideoCapture:
    def __init__(self, camera:0) -> None:
        self.camera = camera
        self.video_capture = None
        self.grabbing = False

        self.frame1 = None
        self.frame2 = None
        self.frame3 = None
        
        self.thread = None
        pass

    def start(self):
        self.grabbing = True
        self.video_capture = cv2.VideoCapture(self.camera)
        self.thread = threading.Thread(target=self.grab)
        self.thread.start()
        return self

    def grab(self):
        while self.grabbing:
            ret, self.frame1 = self.video_capture.read()
            self.frame2 = self.frame1.copy()
            self.frame3 = self.frame1.copy()
            pass

    def stop(self):
        self.video_capture.release()
        self.grabbing = False
    