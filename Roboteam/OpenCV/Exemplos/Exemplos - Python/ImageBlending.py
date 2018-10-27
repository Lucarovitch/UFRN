import cv2
import numpy as np

# NOT WORKING!!!

A = cv2.imread('apple.png')
B = cv2.imread('orange.png')
w, h, _ = A.shape
B = cv2.resize(B, (300, 300))
A = cv2.resize(A, (300, 300))
#cv2.imshow('A', A)
#cv2.imshow('B', B)
print(A.shape)
print(B.shape)
#cv2.waitKey(0)

# generate Gaussian pyramid for A - 6 levels
G = A.copy()
gpA = [G]
for i in range(6):
    G = cv2.pyrDown(G)
    gpA.append(G)

# generate Gaussian pyramid for B - 6 levels
G = B.copy()
gpB = [G]
for i in range(6):
    G = cv2.pyrDown(G)
    gpB.append(G)

# generate Laplacian Pyramid for A
lpA = [gpA[5]]
for i in range(5, 0, -1):
    GE = cv2.pyrUp(gpA[i])
    gpA[i - 1] = cv2.resize(gpA[i - 1], (GE.shape[0], GE.shape[0]))
    L = cv2.subtract(gpA[i - 1], GE)
    lpA.append(L)

# generate Laplacian Pyramid for B
lpB = [gpB[5]]
for i in range(5, 0, -1):
    GE = cv2.pyrUp(gpB[i])
    gpA[i - 1] = cv2.resize(gpA[i - 1], (GE.shape[0], GE.shape[0]))
    L = cv2.subtract(gpB[i - 1], GE)
    lpB.append(L)

# Now add left and right halves of images in each level
LS = []
for la,lb in zip(lpA, lpB):
    rows, cols, dpt = la.shape
    ls = np.hstack((la[:, 0:cols / 2 ], lb[:, cols / 2 :]))
    LS.append(ls)

# now reconstruct
ls_ = LS[0]
for i in range(1, 6):
    ls_ = cv2.pyrUp(ls_)
    ls_ = cv2.add(ls_, LS[i])

# image with direct connecting each half
real = np.hstack((A[:,:cols/2],B[:,cols/2:]))

cv2.imshow('Pyramid_blending2.jpg', ls_)
cv2.imshow('Direct_blending.jpg', real)