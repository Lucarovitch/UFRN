import cv2
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread('j.png', 0)

kernel = np.ones((5,5),np.uint8)                                # Structuring element square
kernel2 = cv2.getStructuringElement(cv2.MORPH_CROSS, (12, 12))  # Structuring element ellipticd

erosion = cv2.erode(img,kernel,iterations = 1)                  # Truncates all pixels non zero
dilation = cv2.dilate(img,kernel,iterations = 1)                # If at lest one pixel is 1 on kernel
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel2)         # Erosion + Dilatation - Background Noise
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel2)        # Dilatation + Erosion - Foreground Noise
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)    # Diference in Dilatation and Erosion
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel2)        # Diference in Image and Opening
blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel2)    # Diference in Image and Closing


plt.subplot(241), plt.imshow(img), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(242), plt.imshow(erosion), plt.title('Erosion')
plt.xticks([]), plt.yticks([])
plt.subplot(243),plt.imshow(dilation),plt.title('Dilatation Ex')
plt.xticks([]), plt.yticks([])
plt.subplot(244),plt.imshow(opening),plt.title('Openining Ex')
plt.xticks([]), plt.yticks([])
plt.subplot(245),plt.imshow(closing),plt.title('Closing Ex')
plt.xticks([]), plt.yticks([])
plt.subplot(246),plt.imshow(gradient),plt.title('Gradient Ex')
plt.xticks([]), plt.yticks([])
plt.subplot(247),plt.imshow(tophat),plt.title('Top Hat ex')
plt.xticks([]), plt.yticks([])
plt.subplot(248),plt.imshow(blackhat),plt.title('Black Hat ex')
plt.xticks([]), plt.yticks([])
plt.show()