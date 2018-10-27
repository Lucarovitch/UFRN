import numpy as np
import cv2

def VideoContour(treatment, thresholdvalue1, thresholdvalue2, minimumperimeter, maximumperimeter, displaynumberofcontours): 
	"""
	Function to draw the contours in a video 
	Parameters:
	treatment  define the treatment type in order to make the image binary, the two types presented here are using the Canny function and the Threshold function
	thresholdvalue1	first threshold for the hysteresis procedure. if the treatment type is threshold, then it sets the threshold value.
	thresholdvalue2	second threshold for the hysteresis procedure.
	minimumperimeter sets the minimum perimeter value for the contours to be drawn
	maximumperimeter sets the maximum perimeter value for the contours to be drawn
	displaynumberofcontours 'yes' print the contour vector length, else does not print anything
	"""
	# Define which camera you will use (0) for default
	cap = cv2.VideoCapture(0)
	# Define the codec and create VideoWriter object
	fourcc = cv2.VideoWriter_fourcc(*'XVID')
	out = cv2.VideoWriter('output.avi',fourcc, 20.0, (150,150))
	while(cap.isOpened()):
	    # Capture frame-b	y-frame
	    ret, frame = cap.read()
	    imgray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	    # Check which treatment will be done
	    if treatment == 'canny' or treatment == 'Canny':
	    	binaryimage = cv2.Canny(imgray,thresholdvalue1,thresholdvalue2)
	    elif treatment == 'threshold' or treatment == 'thresh' or treatment == 'Threshold' or  treatment == 'Thresh':
	    	ret, binaryimage = cv2.threshold(imgray, thresholdvalue1, 255, cv2.THRESH_BINARY)
	    else:
	    	print("Invalid image treatment type, in order to find the contours, the image must be binary!")
	    	break;
	    # Find contours 
	    image, contours, hierarchy = cv2.findContours(binaryimage, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	    # Check if the user wants the number of contours to be displayed
	    if displaynumberofcontours == 'yes' or  displaynumberofcontours ==  'Yes' or displaynumberofcontours ==  'y':
	    	print(len(contours))

	    for index, c in enumerate(contours): 
	    	# Apply the filter based on perimeters          
	    	if (cv2.arcLength(c,True) > minimumperimeter) and (cv2.arcLength(c,True) < maximumperimeter):
	    		#Draw contours
	    		img = cv2.drawContours(frame, contours, index, (0, 255, 0), 3)
	    # Display the resulting frame
	    cv2.imshow('frame', img)
	    # Wait for the button 'q' to finish the process
	    if cv2.waitKey(1) & 0xFF == ord('q'):
	        break

	# When everything done, release the capture
	cap.release()
	out.release()
	cv2.destroyAllWindows()

VideoContour('canny', (255/3), 255, 200, 2000, 'n')

"""
Good calls of the function: 
VideoContour('canny', (255/3), 255, 200, 2000, 'n')

"""