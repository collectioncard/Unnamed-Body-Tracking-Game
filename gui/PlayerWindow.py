from PyQt5.QtWidgets import QMainWindow, QLabel

from trackingSystem.TrackerHandler import TrackerHandler


class PlayerWindow(QMainWindow):
    def __init__(self, poseTracker: TrackerHandler):
        super().__init__()
        self.setWindowTitle("Player Window")
        self.setCentralWidget(QLabel("Player Window"))
