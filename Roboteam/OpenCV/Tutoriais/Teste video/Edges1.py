import numpy as np
import cv2
M = []
cap = cv2.VideoCapture(0)
# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('outputEdges.avi',fourcc, 20.0, (640,480), isColor = False)
while(cap.isOpened()):
    # Capture frame-b	y-frame
    ret, frame = cap.read()
    
    # Our operations on the frame come here
    	#gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #frame = cv2.Canny(frame,200,300)
    imgray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(imgray, 127, 255, 0)
    image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    #frame2, contours, hierarchy = cv2.findContours(frame, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    #cv2.drawContours(frame, contours, -1, (0,255,0), 3)
    out.write(imgray)
    # Display the resulting frame
    cnt = contours[4]
    img = cv2.drawContours(frame, [cnt], 0, (0,255,0), 3)
    cv2.imshow('frame', img)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
	
# When everything done, release the capture
cap.release()
out.release()
cv2.destroyAllWindows()
