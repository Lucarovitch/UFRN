import numpy as np
import cv2

# Load an color image in grayscale
img = cv2.imread('teste.jpeg',0)
cv2.imshow('image',img)
cv2.waitKey(0) # Wait for "0" key to proceed 
cv2.destroyAllWindows()
cv2.imwrite('bettagray.png',img)

