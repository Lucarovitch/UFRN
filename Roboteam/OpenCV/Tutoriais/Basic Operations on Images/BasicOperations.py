
# coding: utf-8

# In[1]:


import cv2
import numpy as np
from matplotlib import pyplot as plt
img1 = cv2.imread('spfc.png')
plt.subplot(211),plt.imshow(img1,'gray'),plt.title('SPFC')
img2 = cv2.imread('OpenCV_Logo_with_text.png')
plt.subplot(212),plt.imshow(img2,'gray'),plt.title('OpenCV')
dst = cv2.addWeighted(img1,0.7,img2,0.3,0)
plt.subplot(213),plt.imshow(dst,'gray'),plt.title('OpenCV+SPFC')
plt.show()
