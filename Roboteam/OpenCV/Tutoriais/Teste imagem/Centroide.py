import cv2
import numpy as np

# Finding Contour and Moments
img = cv2.imread('testContours.png')
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 127, 255, 0)
_, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#for c in contours:
#    im = cv2.drawContours(img, [c], 0, (0, 255, 0), 3)


M = []
C = []
for c in contours
	# Moments os the contours are in hierarchy variable       
    M.append(cv2.moments(c))    

    # Centroid of all contours
    C.append([int(M[index]['m10']/M[index]['m00']), int(M[index]['m01']/M[index]['m00'])])
print(C)
#img = cv2.circle(img, tuple(C[index]), 2, (255, 0, 0), 2)
#cv2.imshow('Original', img)
#cv2.waitKey(0)