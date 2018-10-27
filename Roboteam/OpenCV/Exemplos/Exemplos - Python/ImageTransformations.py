import cv2
import numpy as np

### Resizing
img = cv2.imread('messi.jpg')
#cv2.imshow('original', img)
# 2 Types of interpolation for resizing
res = cv2.resize(img, None, fx=2, fy=2, interpolation = cv2.INTER_LINEAR) # Faster Generally Worse
# cv2.imshow('resize LINEAR INTERPOLATION',res)
height, width, _ = img.shape
res = cv2.resize(img, (2*width, 2*height), interpolation = cv2.INTER_CUBIC) # Slower Generally Better
# cv2.imshow('resize CUBIC INTERPOLATION',res)

### Translation
xtranslation = 0
ytranslation = 0
M_trans = np.float32([[1, 0, xtranslation],[0, 1, ytranslation]]) # Transform Matrix
dst = cv2.warpAffine(img, M_trans, (width, height))
# cv2.imshow('img', dst)

### Rotation
rotation_center = (width / 2, height / 2) # tuple with x, y coordinates
angle_in_degrees = 90
scale = 1
M_rot = cv2.getRotationMatrix2D( rotation_center, angle_in_degrees, scale)
rdst = cv2.warpAffine(img, M_rot,(width, height))
#cv2.imshow('rotated', rdst)

img_1 = cv2.imread('test.png',0)
cv2.imshow('original', img_1)

# Affine Transformation
width, height = img_1.shape
pts1 = np.float32([[50,50],[200,50],[50,200]])      # 3 points position in first image
pts2 = np.float32([[10,100],[200,50],[100,250]])    # 3 points position in new image
M_affine = cv2.getAffineTransform(pts1,pts2)
adst = cv2.warpAffine(img_1, M_affine, (width, height))
#cv2.imshow('affined', adst)

# Perspective Transformation
pts1 = np.float32([[56,75],[368,45],[20,387],[380,390]])    # 4 poinst for perspective transformation input image
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])        # 4 poinst for perspective transformation output image
M_pers = cv2.getPerspectiveTransform(pts1,pts2)

pdst = cv2.warpPerspective(img_1, M_pers, (500, 500))
cv2.imshow('persoective', pdst)

cv2.waitKey(0)
cv2.destroyAllWindows()