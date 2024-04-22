import time

import cv2
import mediapipe as mp


class PoseTracker:
    def __init__(self):
        self.result = mp.tasks.vision.PoseLandmarkerResult
        self.landmarker = mp.tasks.vision.PoseLandmarker
        self.createLandmarker()

    def createLandmarker(self):

        #create callback function to get the detected landmarks on each frame
        def updateResult(result, image, time):
            self.result = result

        options = mp.tasks.vision.PoseLandmarkerOptions(
            base_options=mp.tasks.BaseOptions(model_asset_path="pose_landmarker.task"),
            running_mode=mp.tasks.vision.RunningMode.LIVE_STREAM,
            result_callback=updateResult
        )

        self.landmarker = self.landmarker.create_from_options(options)

    def detectPoints(self, frame):
        convertedImage = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame)
        self.landmarker.detect_async(image=convertedImage, timestamp_ms=int(time.time() * 1000))

    def close(self):
        # close landmarker
        self.landmarker.close()

