import cv2
import numpy as np

# Finding Contour and Moments
img = cv2.imread('testContours.png')
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 127, 255, 0)
_, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#for c in contours:
#    im = cv2.drawContours(img, [c], 0, (0, 255, 0), 3)
cv2.imshow('Original', img)
cv2.waitKey(0)

M = []
C = []
A = []
P = []
Ca = []
H=[]
BRs = []
BRr = []
BC = []
BE = []
index = 0
print(len(contours))

for c in contours:           
    # Moments os the contours are in hierarchy variable       
    M.append(cv2.moments(c))    

    # Centroid of all contours
    C.append([int(M[index]['m10']/M[index]['m00']), int(M[index]['m01']/M[index]['m00'])])
    print(C)
    # Area of  contours can be found 2 methods 
    a1 = M[index]['m00']
    a2 = cv2.contourArea(c)
    if a1 == a2:
        A.append(a1)

    # Perimiter of contour (True arg required for closed curve)
    P.append(cv2.arcLength(c, True))

    # Contour Approximation  - Generally used for shape correction
    epsilon = 0.1*P[index]  # 1% approximation of previous contour
    Ca.append(cv2.approxPolyDP(c, epsilon, True)) # Approximated contour

    # Convex Hull - An exterior polygon that covers the contour ?
    H.append(cv2.convexHull(c))

    # Bounding Shapes
    x, y, w, h = cv2.boundingRect(c)               
    BRs.append([(x, y), (x + w, y + h)])          # Straight Rectangle
    rect = cv2.minAreaRect(c)
    BRr.append(np.intp(cv2.boxPoints(rect)))      # Rotaded Rectangle
    (x, y), radius = cv2.minEnclosingCircle(c)
    BC.append([(int(x), int(y)), int(radius)])    # Circle
    try:
        BE.append(cv2.fitEllipse(c))              # Ellipse
    except:
        pass
    index = index + 1

### DRAWING RESULTS ###
index = 0
# Centroid
#img = cv2.drawContours(img, contours[index], 0, (255, 0, 0), 2)
img = cv2.circle(img, tuple(C[index]), 2, (255, 0, 0), 2)

# Area
#img = cv2.drawContours(img, contours[index + 1], 0, (0,255,0), 2)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, str(A[index + 1]), (C[index + 1][0] + 5, C[index + 1][1] + 5),
            font, 4, (255, 255, 2), 2, cv2.LINE_AA)

# Perimiter of contour (True arg required for closed curve)
#img = cv2.drawContours(img, [contours[index + 2]], 0, (0, 0, 255), 2)
cv2.putText(img, str(P[index + 2]), (C[index + 2][0] + 5, C[index + 1][1] + 5),
            font, 4, (2, 255, 255), 2, cv2.LINE_AA)

# Contour Approximation
img = cv2.drawContours(img, [Ca[index + 3]], 0, (0, 127, 127), 3)

# Convex Hull - An exterior polygon that covers the contour ?
img = cv2.drawContours(img, [H[index + 4]], 0, (127, 127, 127), 3)

# Bounding Shapes
img = cv2.rectangle(img, BRs[index + 5][0], BRs[index + 5][1], (127, 255, 127),2)
img = cv2.drawContours(img, [BRr[index + 6]], 0, (0, 55, 127), 2)
img = cv2.circle(img, BC[index + 7][0], BC[index + 7][1], (12, 55, 20), 2)
img = cv2.ellipse(img, BE[index + 8], (0, 255, 0), 2)

cv2.imshow('Resultados', img)
cv2.waitKey(0)