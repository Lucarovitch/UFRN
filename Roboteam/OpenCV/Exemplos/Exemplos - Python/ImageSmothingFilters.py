import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('opencv.jpg')
#cv2.imshow('original', img)
#cv2.waitKey(0)

# Kernel used
kernel_2dfilter = np.ones((5,5), np.float32)/25 

dst = cv2.filter2D(img, -1, kernel_2dfilter)     # Aplly convolution os given kernel filter
blur = cv2.blur(img,(3,3))              # General blur function for a 3x3 average function
gaus = cv2.GaussianBlur(img,(5,5),0)    # Gaussian Blur
median = cv2.medianBlur(img,5)          # Median Blur
biblur = cv2.bilateralFilter(img, 9, 75, 75) # Bilateral Filter check docs for parameters


plt.subplot(231), plt.imshow(img), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(232),plt.imshow(dst),plt.title('Averaging')
plt.xticks([]), plt.yticks([])
plt.subplot(233),plt.imshow(blur),plt.title('Average Blur')
plt.xticks([]), plt.yticks([])
plt.subplot(234),plt.imshow(gaus),plt.title('Gaussian Blur')
plt.xticks([]), plt.yticks([])
plt.subplot(235),plt.imshow(median),plt.title('Median Blur')
plt.xticks([]), plt.yticks([])
plt.subplot(236),plt.imshow(biblur),plt.title('Bilaterial Blur')
plt.xticks([]), plt.yticks([])
plt.show()