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
old_imgsmall = cv2.resize(old_img, (0,0), fx = 0.5, fy = 0.5)
old_gray = cv2.cvtColor(old_imgsmall,cv2.COLOR_BGR2GRAY)
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
	sens = 2.4
	cont = 0
	for i in range(len(t)-1):
		if(t[i] > x[i]+sens):
			cont = cont + 1	
	if(cont >= 1):
		return True
	else:
		return False
t = [0]*7
b = [0]*7
x = [0]*7
y = [0]*7
print("click na imagem para dar start")
aux = np.array([100,120],dtype=np.float32)
p1 = np.array([100,120],dtype=np.float32)	    
while capture.isOpened():
	cv2.namedWindow('img')
	cv2.setMouseCallback('img',on_mouse,0)
	_,img = capture.read()	
	imgsmall = cv2.resize(img, (0,0), fx = 0.5, fy = 0.5)
	gray_frame = cv2.cvtColor(imgsmall,cv2.COLOR_BGR2GRAY)
	# shape= 480,640
	# Escreva sua regiao de gradiente que quer analizar
	#p1 = np.array([[[286.7,335.6],[286.7,351.6],[293.7,335.6],[286.7,351.6],[300.7,335.6],[300.7,351.6],[307.7,335.6],[307.7,351.6],[314.7,335.6],[314.7,351.6],[321.7,335.6],[321.7,351.6],[328.7,335.6],[328.7,351.6],[335.7,335.6]]],dtype=np.float32)
	for index in range(7):
			aux = np.vstack((aux, np.array([100+index,120],dtype=np.float32)))
			p1 = np.array([aux],dtype = np.float32)			
	p_flag = p1
	for i in range(7):
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
		for i in range(7):
			t[i]=new_point[0,i,0]
			b[i]=new_point[0,i,1]
		#for i in range(19):
			#t1[i]=new_point1[0,i,0]
			#b1[i]=new_point1[0,i,1]
		# Desenhe seus pontos:
		for i in range(len(t)-1):
			cv2.circle(imgsmall,(t[i],b[i]),5,(0,255,0),-1)							
		if(verifica(y,b)):
			print("active")
			teste = np.random.rand()
			if teste<= 0.8:
				print("de comida")
			else:
				print("nao de comida")
			#cv2.imshow('img',img)
			#break
	cv2.imshow('img',imgsmall)
	pressed_key = cv2.waitKey(1) & 0xFF
	if pressed_key == ord("z"):
		break
cv2.destroyAllWindows()
capture.release() 	
	
	
			

