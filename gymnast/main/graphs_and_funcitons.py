import numpy as np
import os
import cv2
from PIL import Image


def angle(a, b, c):

    ba = a - b
    bc = c - b

    cosine_angle = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc))
    angle = np.arccos(cosine_angle)

    print(angle)
    np.degrees(angle)


def graph_generators():
    # To be completed
    pass


