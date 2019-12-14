import cv2
import numpy as np

video_path = ""


def get_optical_flow(video_path):
    cap = cv2.VideoCapture(video_path)

    feature_params = dict(maxCorners = 16, qualityLevel = 0.01, minDistance = 3, blockSize = 7)
    lk_params = dict( winSize  = (15,15), maxLevel = 2, criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))
    color = np.random.randint(0,255,(100,3))
    
    width = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    height = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    output = cv2.VideoWriter('sparse_lucas.mp4', cv2.VideoWriter_fourcc(*'MPV4'), 30, (width,height))

    ret,old_frame = cap.read()
    old_gray = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)
    old_points = cv2.goodFeaturesToTrack(old_gray, **feature_params)

    while(1):
        ret, frame = cap.read()
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        new_points, status, err = cv2.calcOpticalFlowPyrLK(old_gray, frame_gray, old_points, None, **lk_params)

        good_new = new_points[status==1]


    # old_gray = 


    