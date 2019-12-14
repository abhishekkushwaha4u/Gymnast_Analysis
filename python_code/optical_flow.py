import cv2
import numpy as np

video_path = ""


def get_optical_flow(video_path):
    cap = cv2.VideoCapture(video_path)

    # feature_params = dict(maxCorners = 100, qualityLevel = 0.3, minDistance = 7, blockSize = 7)
    lk_params = dict( winSize  = (15,15), maxLevel = 2, criteria = (cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 0.03))
    color = np.random.randint(0,255,(100,3))
    
    


    
    ret, old_frame = cap.read()
    # old_gray = 


    