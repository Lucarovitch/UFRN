#### Using OpticalFlow to track a ROI
import numpy as np
import cv2
import time



point_selected = False
point_new= False
point = np.array([[[]]],dtype=np.float32)
old_point = np.array([])
global pt,xm,ym
pt = np.array([[]],dtype=np.float32)
b = np.array([[]],dtype=np.float32)


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
global contador 
contador = 0

def on_mouse(event,x,y,flags,params):
	global point,point_selected,old_points,xm,ym,contador,point_new
	if event == cv2.EVENT_LBUTTONDOWN:
		print('Start Mouse Position:' ,str(x),str(y))
		xm = np.float32(x)
		ym = np.float32(y)
		contador = contador + 1
		point_selected = True
		point_new = True
# verifica se houve agitacao
def verifica(x1,x2,x3,x4,t1,t2,t3,t4):
	sens = 1.
	cont = 0
	if(t1 > x1+sens or t1 < x1-sens):
		cont = cont + 1		
	if(t2 > x2+sens or t2 < x2-sens):
		cont = cont + 1	
	if(t3 > x3+sens or t3 < x3-sens):
		cont = cont + 1	
	if(t4 > x4+sens or t4 < x4-sens):
		cont = cont + 1
	if(cont >= 3):
		return True
	else:
		return False

	
print("click na imagem para dar start")
val = np.array([[45.7,89.6],[45.7,79.6],[35.7,79.6],[35.7,89.6]],dtype=np.float32)
p1 = np.array([[[45.7,89.6],[45.7,79.6],[35.7,79.6],[35.7,89.6]]],dtype=np.float32)
inter = val	    
while capture.isOpened():
	cv2.namedWindow('img')
	cv2.setMouseCallback('img',on_mouse,0)
	ret,img = capture.read()	
	gray_frame = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	# Escreva sua regiao de gradiente que quer analizar
    #
	p_flag = p1
	x1,y1 = (p_flag[0,0,0],p_flag[0,0,1])
	x2,y2 = (p_flag[0,1,0],p_flag[0,1,1])
	x3,y3 = (p_flag[0,2,0],p_flag[0,2,1])
	x4,y4 = (p_flag[0,3,0],p_flag[0,3,1])
	if ret is not None:
		if point_new == True:
			print("entrou")
			b = np.array([[[xm,ym]]],dtype=np.float32)
			val = np.vstack( (val,np.array([[xm,ym]])) )
			p1 = np.array([val],dtype=np.float32)
			point_new = False
			# apresenta um erro, onde os pontos voltam para seu valor inicial
		#print("b=",b)
		#print("contador=",contador)
		#val = np.concatenate((p1,b),axis=1)
		#val = np.append(p1,b,axis=1)
		#val = np.vstack( (val,np.array([[xm,ym]])) )  pode tirar aki, so fiz isso para perimitir o if ali em cima
		print("val=",val)
		#p1 = np.array([val],dtype=np.float32)
		print("val_new=",p1)
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
		#t1 = new_point[0,0,0]
		#b1 = new_point[0,0,1]
		#t2 = new_point[0,1,0]
		#b2 = new_point[0,1,1]
		#t3 = new_point[0,2,0]
		#b3 = new_point[0,2,1]
		#t4 = new_point[0,3,0]
		#b4 = new_point[0,3,1]
		for i in range(contador+3):
			cv2.circle(img,(new_point[0,i,0],new_point[0,i,1]),5,(0,255,0),-1)
		# Desenhe seus pontos:
		#cv2.circle(img,(t1,b1),5,(0,255,0),-1)
		#cv2.circle(img,(t2,b2),5,(0,255,0),-1)	
		#cv2.circle(img,(t3,b3),5,(0,255,0),-1)	
		#cv2.circle(img,(t4,b4),5,(0,255,0),-1)
		#cv2.circle(img,(t5,b5),5,(0,255,0),-1)			
		#if(verifica(x1,x2,x3,x4,t1,t2,t3,t4)):
			#print("active")
	cv2.imshow('img',img)
	pressed_key = cv2.waitKey(1) & 0xFF
	if pressed_key == ord("z"):
		break
cv2.destroyAllWindows()
capture.release() 	
	
	
			

