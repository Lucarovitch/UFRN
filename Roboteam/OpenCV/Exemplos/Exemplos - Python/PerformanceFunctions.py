import cv2
import numpy as np

####### GOOD PRACTICES #######

# 1 Avoid using loops in Python as far as possible, especially double/triple loops etc. They are inherently slow.
# 2 Vectorize the algorithm/code to the maximum possible extent because Numpy and OpenCV are optimized for vector operations.
# 3 Exploit the cache coherence.
# 4 Never make copies of array unless it is needed. Try to use views instead. Array copying is a costly operation.

img1 = cv2.imread('messi.jpg')

# check if CPU supports optimized functions calls
print(cv2.useOptimized())

e1 = cv2.getTickCount()
for i in range(5,65,4):
    img1 = cv2.medianBlur(img1,i)
    cv2.imshow('img blur'+str(i),img1)
e2 = cv2.getTickCount()
topen = (e2 - e1)/cv2.getTickFrequency()

print(topen)

k = cv2.waitKey(0) & 0xFF
if k == 27:
    cv2.destroyAllWindows()

