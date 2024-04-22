import time
import cv2
import trackingSystem.PoseTracker
import mediapipe as mp
import numpy as np
from mediapipe.framework.formats import landmark_pb2


class VideoOverlay:

    def drawPointsOnFrame(self, image, trackerResult: mp.tasks.vision.PoseLandmarkerResult):

        try:
            pose_landmarks_list = trackerResult.pose_landmarks
            annotated_image = np.copy(image)

            # Loop through the detected poses to visualize.
            for idx in range(len(pose_landmarks_list)):
                pose_landmarks = pose_landmarks_list[idx]

                # Draw the pose landmarks.
                pose_landmarks_proto = landmark_pb2.NormalizedLandmarkList()
                pose_landmarks_proto.landmark.extend([
                    landmark_pb2.NormalizedLandmark(x=landmark.x, y=landmark.y, z=landmark.z) for landmark in
                    pose_landmarks
                ])
                mp.solutions.drawing_utils.draw_landmarks(
                    annotated_image,
                    pose_landmarks_proto,
                    mp.solutions.pose.POSE_CONNECTIONS,
                    mp.solutions.drawing_styles.get_default_pose_landmarks_style())
            return annotated_image
        except:
            return image