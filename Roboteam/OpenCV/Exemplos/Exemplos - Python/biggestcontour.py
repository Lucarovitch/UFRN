import cv2
import numpy as np

# Copy
#image = image.copy()
image = cv2.imread('testContours.png')
imgray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 127, 255, 0)
#input, gives all the contours, contour approximation compresses horizontal,
#vertical, and diagonal segments and leaves only their end points. For example,
#an up-right rectangular contour is encoded with 4 points.
#Optional output vector, containing information about the image topology.
#It has as many elements as the number of contours.
#we dont need it
_, contours, hierarchy = cv2.findContours(imgray, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

# Isolate largest contour
contour_sizes = [(cv2.contourArea(contour), contour) for contour in contours]
biggest_contour = max(contour_sizes, key=lambda x: x[0])[1]
cv2.imshow('Resultados', image)
cv2.waitKey(0)
mask = np.zeros(image.shape, np.uint8)
cv2.drawContours(image, [biggest_contour], -1, 255, -1)
