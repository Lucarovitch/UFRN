import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('opencv.jpg',0)


e1 = cv2.getTickCount()
edges_slow = cv2.Canny(img, 100, 200, True)
e2 = cv2.getTickCount()
t_slow = (e2 - e1)/cv2.getTickFrequency()

e1 = cv2.getTickCount()
edges_fast = cv2.Canny(img, 10, 100)
e2 = cv2.getTickCount()
t_fast = (e2 - e1) / cv2.getTickFrequency()

combined = cv2.bitwise_xor(edges_fast, edges_slow)

plt.subplot(221),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(223),plt.imshow(edges_slow, cmap = 'gray')
plt.title('Edge Image Slow'), plt.xticks([]), plt.yticks([])
plt.subplot(224),plt.imshow(edges_fast, cmap = 'gray')
plt.title('Edge Image Fast'), plt.xticks([]), plt.yticks([])
plt.subplot(222),plt.imshow(combined, cmap = 'gray')
plt.title('Combined Results'), plt.xticks([]), plt.yticks([])
print("Slow time: " + str(t_slow))
print("Fast time: " + str(t_fast))
plt.show()
