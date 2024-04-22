import cv2
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QPushButton, QWidget, QApplication

from gui.AudWindow import AudWindow
from gui.PlayerWindow import PlayerWindow

import trackingSystem.TrackerHandler


#The mod window is gonna basically be the brains for everything I guess. The other two windows will pull form it

class ModWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Moderator Window")
        self.setCentralWidget(QLabel("Moderator Window"))

        #get a reference to the pose tracking system
        self.poseTracker = trackingSystem.TrackerHandler.TrackerHandler()

        #buttons
        boxLayout = QVBoxLayout()

        spawnPlayerWindowButton = QPushButton("Spawn Player Window")
        spawnPlayerWindowButton.clicked.connect(self.showPlayerWindow)
        boxLayout.addWidget(spawnPlayerWindowButton)

        spawnAudWindowButton = QPushButton("Spawn Audience Window")
        spawnAudWindowButton.clicked.connect(self.showAudWindow)
        boxLayout.addWidget(spawnAudWindowButton)

        widgetLayout = QWidget()
        widgetLayout.setLayout(boxLayout)
        self.setCentralWidget(widgetLayout)

        timer = QTimer(self)
        timer.timeout.connect(self.updateVideo)
        timer.start()

        self.video = QLabel(self)
        boxLayout.addWidget(self.video)
        self.video.setFixedSize(640, 480)

    def updateVideo(self):
        frame = self.poseTracker.getTrackedFrame()
        self.video.setPixmap(frame.scaled(self.video.size(), Qt.KeepAspectRatio))

    def showPlayerWindow(self):
        self.playerWindow = PlayerWindow(self.poseTracker)
        self.playerWindow.show()

    def showAudWindow(self):
        self.audWindow = AudWindow(self.poseTracker)
        self.audWindow.show()
