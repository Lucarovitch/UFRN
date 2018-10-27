import numpy as np
import cv2
M = []
C = []
index = 1
cap = cv2.VideoCapture(0)
# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))
while(cap.isOpened()):
    # Capture frame-b	y-frame
    ret, frame = cap.read()

    imgray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #ret, thresh = cv2.threshold(imgray, 200, 255, cv2.THRESH_BINARY)
    canny = cv2.Canny(imgray,200,300)
    image, contours, hierarchy = cv2.findContours(canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnt = contours[-1]
    img = cv2.drawContours(frame, [cnt], 0, (0,255,0), 3)
    for c in contours

        # Moments os the contours are in hierarchy variable       
        M.append(cv2.moments(cnt))  

        # Centroid of all contours
        C.append([int(M[index]['m10']/M[index]['m00']), int(M[index]['m01']/M[index]['m00'])])
        out.write(frame)
        # Our operations on the frame come here
    	#gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #edges = cv2.Canny(frame,100,200)
    # Display the resulting frame
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
out.release()
cv2.destroyAllWindows()
