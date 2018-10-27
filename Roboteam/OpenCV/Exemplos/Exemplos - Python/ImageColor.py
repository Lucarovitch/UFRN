import cv2
import numpy as np

img_color = cv2.imread('test.png')
px = img_color[100, 100]
print(px)
cv2.imshow('Image Color', img_color)

img_gray = cv2.imread('test.png', 0)
px = img_gray[100, 100]
print(px)
cv2.imshow('Image Gray', img_gray)

cv2.waitKey(0)
cv2.destroyAllWindows()