import cv2
import numpy as np
from matplotlib import pyplot as plt

# Global Histogram Equalization
img = cv2.imread('CLAHE.jpg', 0)
equ = cv2.equalizeHist(img)
font = cv2.FONT_HERSHEY_SIMPLEX

# CLAHE (Contrast Limited Adaptive Histogram Equalization)
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize = (8, 8))  # create a CLAHE object (optional args)
cl1 = clahe.apply(img)

cv2.putText(img, "Original", (50, 50),
            font, 1, (255, 255, 255), 3, cv2.LINE_AA)

cv2.putText(equ, "Equalized Histogram", (50, 50),
            font, 1, (255, 255, 255), 3, cv2.LINE_AA)

cv2.putText(cl1, "Clahe", (50, 50),
            font, 1, (255, 255, 255), 3, cv2.LINE_AA)

res = np.hstack((img, equ, cl1))      # Stacking images horizontally
cv2.imshow('Result', res)
cv2.waitKey(0)
