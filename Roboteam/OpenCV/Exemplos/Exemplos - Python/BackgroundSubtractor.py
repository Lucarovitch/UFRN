import numpy as np
import cv2
def BackgroundSubractor():
	"""
	Function that extracts the moving foreground from static background.
	"""
	# Define which camera you will use (0) for default
	cap = cv2.VideoCapture(0)
	# Define the codec and create VideoWriter object
	fourcc = cv2.VideoWriter_fourcc(*'XVID')
	out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))
	#Use the apply the background subtraction algorithm in form of a mask
	fgbg = cv2.createBackgroundSubtractorMOG2()

	while(1):
		#Read frame
	    ret, frame = cap.read()
	    #Apply mask
	    fgmask = fgbg.apply(frame)

	    image, contours, hierarchy = cv2.findContours(fgmask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	    # Check if the user wants the number of contours to be displayed
	    #if displaynumberofcontours == 'yes' or  displaynumberofcontours ==  'Yes' or displaynumberofcontours ==  'y':
	    print(len(contours))

	    for index, c in enumerate(contours): 
	    	# Apply the filter based on perimeters          

	    	if (cv2.arcLength(c,True) > 200) and (cv2.arcLength(c,True) < 2000):
	    		#Draw contours
	    		img = cv2.drawContours(frame, contours, index, (0, 255, 0), 3)
	    	else:
	    		img = frame
	    # Display the resulting frame
	    cv2.imshow('frame', img)
	 	#Show the normal image
	    cv2.imshow('fgmask',frame)
	    #Show the "masked" image
	    cv2.imshow('frame',fgmask)
	    #Finishes the function when the button 'q' is pressed
	    if cv2.waitKey(1) & 0xFF == ord('q'):
	        break
	    

	cap.release()
	cv2.destroyAllWindows()

BackgroundSubractor()