#### Using OpticalFlow to track a ROI
#### For the aquario em cruz: usando gradiente

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
p2 = None
def on_mouse(event,x,y,flags,params):
	global point,point_selected,old_points,x1,y1
	if event == cv2.EVENT_LBUTTONDOWN:
		print('Start Mouse Position:' ,str(x),str(y))
		x1 = np.float32(x)
		y1 = np.float32(y)
		point=(x1,y1)
		#p1 = np.array([[[x1,y1]]],dtype=np.float32)
		point_selected = True
# verifica se houve agitacao
def verifica(x,t):
	sens = 5.
	cont = 0
	for i in range(len(t)-1):
		if(t[i] > x[i]+sens):
			cont = cont + 1	
	if(cont >= 1):
		return True
	else:
		return False
t = [0]*28
b = [0]*28
x = [0]*28
y = [0]*28
p1 = np.array([200,335.6],dtype=np.float32)
aux = np.array([200,335.6],dtype=np.float32)
print("click na imagem para dar start")	    
while capture.isOpened():
	cv2.namedWindow('img')
	cv2.setMouseCallback('img',on_mouse,0)
	_,img = capture.read()	
	gray_frame = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	# shape= 480,640
	# Escreva sua regiao de gradiente que quer analizar
	#p1 = np.array([[[280.7,335.6],[285.7,335.6],[290.7,335.6],[295.7,335.6],[397.7,335.6],[306.7,335.6],[315.7,335.6],[325.7,335.6],[332.7,335.6],[345.7,335.6],[350.7,335.6],[360.7,335.6],[367.7,335.6],[385.7,335.6],[395.7,335.6],[402.7,335.6],[410.7,335.6],[415.7,335.6],[420.7,335.6],[280.7,335.6],[285.7,335.6],[290.7,335.6],[295.7,335.6],[397.7,335.6],[306.7,335.6],[315.7,335.6],[325.7,335.6],[332.7,335.6],[345.7,335.6],[350.7,335.6],[360.7,335.6],[367.7,335.6],[385.7,335.6],[395.7,335.6],[402.7,335.6],[410.7,335.6],[415.7,335.6],[420.7,335.6]]],dtype=np.float32)
	#p_flag = p1
	for index in range(28):
			aux = np.vstack((aux, np.array([200+10*index,335.6],dtype=np.float32)))
			p1 = np.array([aux],dtype = np.float32)
	p_flag = p1

	for i in range(28):
		x[i]  = p_flag[0,i,0]
		y[i]  = p_flag[0,i,1]
	if point_selected == True:
		#print("p_flag=",p_flag)
		new_point,status,error = cv2.calcOpticalFlowPyrLK(old_gray, gray_frame,p1,None,**lk_params)
		# firulagem da documentacao aki em baixo
		#good_new = new_point[status==1]
		#good_old = p0[status==1]
		#p0 = good_new.reshape(-1,1,2)
		# aki comeca o certo -
		#print("new point=",new_point)
		old_gray = gray_frame.copy()
		p1 = new_point
		# atualize seu gradiente:
		for i in range(28):
			t[i]=new_point[0,i,0]
			b[i]=new_point[0,i,1]
		#for i in range(19):
			#t1[i]=new_point1[0,i,0]
			#b1[i]=new_point1[0,i,1]
		# Desenhe seus pontos:
		for i in range(len(t)-1):
			cv2.circle(img,(t[i],b[i]),5,(0,255,0),-1)							
		if(verifica(y,b)):
			print("active")
			#break
	cv2.imshow('img',img)
	pressed_key = cv2.waitKey(1) & 0xFF
	if pressed_key == ord("z"):
		break
cv2.destroyAllWindows()
capture.release() 	
	
	
			

