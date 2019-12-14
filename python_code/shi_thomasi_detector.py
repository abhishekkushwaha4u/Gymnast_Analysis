import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("E:\Aditya\AI_DL_ML\Projects\Gymnast_Analysis\img_black_img53.png")
img = np.array(img, dtype=np.uint8)
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

max_corners = 16
corners = cv2.goodFeaturesToTrack(img2, maxCorners=max_corners, qualityLevel=0.01, minDistance=0.2)

for i in corners:
    x,y = i.ravel()
    cv2.circle(img2,(x,y),10,(255,0,0), 3)

plt.imshow(img2[...,::-1])

img2_rgb = cv2.cvtColor(img2, cv2.COLOR_GRAY2BGR)
cv2.imwrite('stick_track.png',img2_rgb)
plt.show()

