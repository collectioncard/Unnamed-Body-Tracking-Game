import cv2
import trackingSystem.VideoOverlay as VideoOverlay
import trackingSystem.PoseTracker as PoseTracker
from PyQt5.QtGui import QImage, QPixmap


# This class should handle all of our tracking stuff.
class TrackerHandler:

    def __init__(self):
        self.videoCapture = cv2.VideoCapture(0)
        self.poseTracker = PoseTracker.PoseTracker()
        self.vidOverlay = VideoOverlay.VideoOverlay()

    def getOriginalFrame(self):
        ret, frame = self.videoCapture.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(image)
            return pixmap


    def getTrackedFrame(self):
        ret, frame = self.videoCapture.read()
        if ret:
            frame = cv2.flip(frame, 1)
            self.poseTracker.detectPoints(frame)

            frame = self.vidOverlay.drawPointsOnFrame(frame, self.poseTracker.result)



            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(image)
            return pixmap
