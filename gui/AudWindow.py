from PyQt5.QtWidgets import QMainWindow, QLabel

from trackingSystem.TrackerHandler import TrackerHandler


class AudWindow(QMainWindow):
    def __init__(self, poseTracker: TrackerHandler):
        super().__init__()
        self.setWindowTitle("Audience Window")
        self.setCentralWidget(QLabel("Audience Window"))

