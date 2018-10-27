import cv2
import numpy as np
def Centroids(image):
    """
    Function made for drawing the contours and showing the centroids in a image.
    Parameters:
    image The image you want to verify the contours.
    """
    #Reading image
    img = cv2.imread(image)
    #Treating image
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(imgray, 150, 255, 0)
    cv2.imshow('imgthresh', thresh)
    cv2.waitKey(0)
    #Finding contours
    _, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    M = []
    C = []
    P = []

    index = 0
    for c in contours:           
        # Moments os the contours are in hierarchy variable       
        M.append(cv2.moments(c))    

        # Centroid of all contours
        P.append(cv2.arcLength(c,True))
        C.append([int(M[index]['m10']/M[index]['m00']), int(M[index]['m01']/M[index]['m00'])])
        #Drawing centroid of the contours
        img = cv2.circle(img, tuple(C[index]), 2, (255, 0, 0), 2)
        #Drawing contours
        cv2.drawContours(img, contours, index, (0, 255, 0), 3)
        index = index + 1

    index = 0
    print("The centroids are:", C)
    cv2.imshow('Resultados', img)
    cv2.waitKey(0)

Centroids('teste2.png')