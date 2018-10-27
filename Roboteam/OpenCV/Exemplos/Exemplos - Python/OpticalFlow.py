#### Using OpticalFlow to track a ROI
import numpy as np
import cv2
import time



point_selected = False
point = ()
old_point = np.array([])
global pt
pt = np.array([[]],dtype=np.float32)


lk_params = dict(winSize = (15,15),maxLevel=4,
             criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT,10,0.03))

feature_params = dict(maxCorners= 100, qualityLevel = 0.3,
                  minDistance = 7, blockSize = 7)


capture = cv2.VideoCapture(0)
_,old_img = capture.read()
old_gray = cv2.cvtColor(old_img,cv2.COLOR_BGR2GRAY)
p0 = cv2.goodFeaturesToTrack(old_gray, mask = None, **feature_params)
mask = np.zeros_like(old_img)
p1 = None

def on_mouse(event,x,y,flags,params):
	global point,point_selected,old_points,x1,y1
	if event == cv2.EVENT_LBUTTONDOWN:
		print('Start Mouse Position:' ,str(x),str(y))
		x1 = np.float32(x)
		y1 = np.float32(y)
		point=(x1,y1)
		#p1 = np.array([[[x1,y1]]],dtype=np.float32)
		point_selected = True
		

while capture.isOpened():
	cv2.namedWindow('img')
	cv2.setMouseCallback('img',on_mouse,0)
	_,img = capture.read()	
	gray_frame = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	p1 = np.array([[[45.7,89.6]]],dtype=np.float32)
	p_flag = p1
	xi = p_flag[0,0,0]
	yi = p_flag[0,0,1]
	if point_selected == True:
		cv2.circle(img,point,5,(0,0,255),2)
		print("p_flag=",p_flag)
		new_point,status,error = cv2.calcOpticalFlowPyrLK(old_gray, gray_frame,p1,None,**lk_params)
		# virulagem da documentacao aki em baixo
		good_new = new_point[status==1]
		good_old = p0[status==1]
		#p0 = good_new.reshape(-1,1,2)
		# aki comeca o certo -
		print("new point=",new_point)
		old_gray = gray_frame.copy()
		p1 = new_point
		t1 = new_point[0,0,0]
		br = new_point[0,0,1]
		cv2.circle(img,(t1,br),5,(0,255,0),-1)	
		if(t1 >= xi+3. and br >= yi+3.):
			print("active")
	cv2.imshow('img',img)
	pressed_key = cv2.waitKey(1) & 0xFF
	if pressed_key == ord("z"):
		break
cv2.destroyAllWindows()
capture.release() 	
	
	
			

