import detector_pose
import cv2
import mediapipe as mp


detector_pose.check_arms_and_alarm()
detector_pose.are_arms_raised()


detector_pose.source.release()
cv2.destroyAllWindows()



