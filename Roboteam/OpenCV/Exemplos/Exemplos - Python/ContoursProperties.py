import cv2
import numpy as np

img = cv2.imread('testContours.png')
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 127, 255, 0)
_, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnt = contours[4]

# Aspect Ratio
x, y, w, h = cv2.boundingRect(cnt)
aspect_ratio = float(w) / h
print(aspect_ratio)

# Extent
area = cv2.contourArea(cnt)
rect_area = w * h
extent = float(area) / rect_area

# Solidity
hull = cv2.convexHull(cnt)
hull_area = cv2.contourArea(hull) 
solidity = float(area) / hull_area

# Orientation
(x,y), (MA, ma), angle = cv2.fitEllipse(cnt)

# Mask and Pixel Points
mask = np.zeros(imgray.shape, np.uint8)
cv2.drawContours(mask, [cnt], 0, 255, -1)
pixelpoints = np.transpose(np.nonzero(mask))
pixelpointscv = cv2.findNonZero(mask)
print(pixelpoints)

# Max value, min value and locations
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(imgray, mask = mask)

