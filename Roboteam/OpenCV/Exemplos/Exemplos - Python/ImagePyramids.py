import cv2
import numpy as np

def appendImgV(img1, img2):
    h1, w1, c = img1.shape
    h2, w2, c = img2.shape
    if c:
        vis = np.zeros((max(h1, h2), w1+w2, c), np.uint8)
    else:
        vis = np.zeros((max(h1, h2), w1+w2), np.uint8)
    vis[:h1, :w1, :] = img1
    vis[:h2, w1:w1+w2, :] = img2
    # vis = cv2.cvtColor(vis, cv2.COLOR_GRAY2BGR)
    return vis

def appendImgH(img1, img2):
    h1, w1, c = img1.shape
    h2, w2, c = img2.shape
    if c:
        vis = np.zeros((h1 + h2, max(w1, w2), c), np.uint8)
    else:
        vis = np.zeros((h1 + h2, max(w1, w2)), np.uint8)
    vis[:h1, :w1] = img1
    vis[h1:h1 + h2, :w2] = img2
    # vis = cv2.cvtColor(vis, cv2.COLOR_GRAY2BGR)
    return vis


high_reso = cv2.imread('messi.jpg')
lower_reso = cv2.pyrDown(high_reso)
lower_reso2 = cv2.pyrDown(lower_reso)
lower_reso3 = cv2.pyrDown(lower_reso2)

temp1 = appendImgV(lower_reso, lower_reso2)
temp2 = appendImgV(temp1, lower_reso3)
res = appendImgH(high_reso, temp2)                        

cv2.imshow('Pyramids', res)
cv2.waitKey(0)


