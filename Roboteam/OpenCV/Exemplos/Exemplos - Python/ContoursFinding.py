# http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_contours/py_contours_begin/py_contours_begin.html#contours-getting-started

import numpy as np
import cv2

im = cv2.imread('testepeixe.jpeg')
imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 127, 255, 0)
image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
print(len(contours))
cnt = contours[4]
img = cv2.drawContours(im, [cnt], 0, (0,255,0), 3)

cv2.imshow('Contours', img)
cv2.waitKey(0)

