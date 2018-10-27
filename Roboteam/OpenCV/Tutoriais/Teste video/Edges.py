import numpy as np
import cv2

cap = cv2.VideoCapture(0)
# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('outputEdges.avi',fourcc, 20.0, (640,480), isColor = False)
while(cap.isOpened()):
    # Capture frame-b	y-frame
    ret, frame = cap.read()
    
    # Our operations on the frame come here
    	#gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame = cv2.Canny(frame,200,300)
    out.write(frame)
    # Display the resulting frame
    cv2.imshow('frame', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
	
# When everything done, release the capture
cap.release()
out.release()
cv2.destroyAllWindows()
