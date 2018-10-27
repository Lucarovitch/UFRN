import cv2
import numpy as np
def findContoursSons(image):
    """
    Function made for drawing the contours that have a father in a image.
    Parameters:
    image The image you want to verify the contours.
    """
    #Reading image
    img = cv2.imread(image)
    #Treating the image
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(imgray, 150, 255, 0)
    cv2.imshow('imgthresh', thresh)
    cv2.waitKey(0)
    _, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    #Initializing variables
    M = []
    C = []
    P = []
    index = 0
    for c in contours: 
        print(hierarchy[0][index][3])
        #Finding contours that have a father and drawing them
        if(hierarchy[0][index][3] != -1):
        	ContornoTemPai = hierarchy[0][index][3]
        	img = cv2.drawContours(img, contours, index, (0, 255, 0), 3)
        index = index + 1
    index = 0


    cv2.imshow('Resultados', img)
    cv2.waitKey(0)

findContoursSons('teste2.png')