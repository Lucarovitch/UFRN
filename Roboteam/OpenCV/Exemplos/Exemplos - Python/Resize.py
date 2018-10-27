import numpy as np
import cv2

capture = cv2.VideoCapture(0)
# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (150,150))
while(capture.isOpened()):
	# Capture frame-b	y-frame
	
	
	_,old_img = capture.read()
	old_imgsmall = cv2.resize(old_img, (0,0), fx = 0.5, fy = 0.5)
	cv2.imshow('frame', old_imgsmall)
	# Wait for the button 'q' to finish the process
	if cv2.waitKey(1) & 0xFF == ord('q'):
	    break
cap.release()
out.release()
cv2.destroyAllWindows()