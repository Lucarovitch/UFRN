#### Using OpticalFlow to track a ROI
# Esse algoritimo nao tem o intuito de rastrear, pois o Lucas kendra
# nao consegue acompanhar grandes agitacoes
import numpy as np
import cv2
import time



point_selected = False                   # informa se voce selecionou o primeiro ponto
point_new= False                         # informa quando voce selecionou um novo ponto
point = np.array([[[]]],dtype=np.float32)# apos o primeiro

global pt,xm,ym                          # pontos x,y do mouse quando selecionado

#pt = np.array([[]],dtype=np.float32)

b = np.array([[]],dtype=np.float32)      # array intermediario para receber os pontos


# parametros Lucas Ked
lk_params = dict(winSize = (15,15),maxLevel=4,
             criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT,10,0.03))
# parametros shi - tasu, nao estou utilizando no momentos
feature_params = dict(maxCorners= 100, qualityLevel = 0.3,
                  minDistance = 7, blockSize = 7)

#capture o primeiro frame
capture = cv2.VideoCapture(0)
_,old_img = capture.read()
# convertar em escala cinza e adicione o parametro shi-tasu
old_gray = cv2.cvtColor(old_img,cv2.COLOR_BGR2GRAY)
p0 = cv2.goodFeaturesToTrack(old_gray, mask = None, **feature_params)
mask = np.zeros_like(old_img)

# variaveis para adicionar pontos no mouse para rastrear e contador para saber quantos pontos adicionados
p1 = None
global contador 
contador = 0

# funcao que permite o uso manual de clicar nos pontos
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
	sens = 2.
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
# pre-pontos para teste e para saber se houve agitacao no gradiente
val = np.array([[45.7,89.6],[45.7,79.6],[35.7,79.6],[35.7,89.6]],dtype=np.float32)
p1 = np.array([[[45.7,89.6],[45.7,79.6],[35.7,79.6],[35.7,89.6]]],dtype=np.float32)
inter = val	    

while capture.isOpened():
	cv2.namedWindow('img')
	cv2.setMouseCallback('img',on_mouse,0)
	ret,img = capture.read()
	gray_frame = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    # flag para indicar agitacao no campo que ja pre-estabelecemos do grad
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
		#print("val_new=",p1)
		new_point,status,error = cv2.calcOpticalFlowPyrLK(old_gray, gray_frame,p1,None,**lk_params)
		old_gray = gray_frame.copy()
		p1 = new_point
		# atualize sua area de interesse:
		t1 = new_point[0,0,0]
		b1 = new_point[0,0,1]
		t2 = new_point[0,1,0]
		b2 = new_point[0,1,1]
		t3 = new_point[0,2,0]
		b3 = new_point[0,2,1]
		t4 = new_point[0,3,0]
		b4 = new_point[0,3,1]
		for i in range(contador+3):
			cv2.circle(img,(new_point[0,i,0],new_point[0,i,1]),5,(0,255,0),-1)	
		# caso haja agitacao
		if(verifica(x1,x2,x3,x4,t1,t2,t3,t4)):
			print("active")
	cv2.imshow('img',img)
	pressed_key = cv2.waitKey(1) & 0xFF
	if pressed_key == ord("z"):
		break
cv2.destroyAllWindows()
capture.release() 	
	
	
			

