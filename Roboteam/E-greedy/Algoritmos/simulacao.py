from visual import *
from visual.graph import *
import math
import numpy as np
from matplotlib import pyplot as plt

scene = display(title='Ambiente')

#BASE

base = box(pos=(0,0,0), length = 70, height = 10 , width = 0.1 , material = materials.wood)
base2 = box(pos=(0,20,0), length = 10, height = 30 , width = 0.1 , material = materials.wood)
base3 = box(pos=(0,-20,0), length = 10, height = 30 , width = 0.1 , material = materials.wood)
linha = box(pos=(0,0,0.1), length=60, height=0.5, width=0.01, color=color.black)
linha = box(pos=(0,0,0.1), length=0.5, height=60, width=0.01, color=color.black)

#BOX.MAGENTA

eixored = frame()
wall1 = box(frame = eixored ,pos = (0,35,4), length = 10 , height = 0.1 , width = 8 , material = materials.wood)
wall2 = box(frame = eixored ,pos = (5,20,4), length = 0.1 , height = 30 , width = 8 , material = materials.wood)
wall3 = box(frame = eixored ,pos = (-5,20,4), length = 0.1 , height = 30 , width = 8 , material = materials.wood)
symbol_magenta = cylinder(frame = eixored, pos=(0,30,0.09), axis = (0,0,1), length= 0.01, radius = 4, color=color.magenta)

#BOX.BLUE

eixoblue = frame()
wall1 = box(frame = eixoblue ,pos = (0,-35,4), length = 10 , height = 0.1 , width = 8 , material = materials.wood)
wall2 = box(frame = eixoblue ,pos = (5,-20,4), length = 0.1 , height = 30 , width = 8 , material = materials.wood)
wall3 = box(frame = eixoblue ,pos = (-5,-20,4), length = 0.1 , height = 30 , width = 8 , material = materials.wood)
symbol_blue = cylinder(frame = eixoblue, pos=(0,-30,0.09), axis = (0,0,1), length= 0.01, radius = 4, color=color.blue)

#EIXO.YELLOW

eixoyellow = frame()
wall1 = box(frame = eixoyellow ,pos = (35,0,4), length = 0.1 , height = 10 , width = 8 , material = materials.wood)
wall2 = box(frame = eixoyellow ,pos = (20,5,4), length = 30 , height = 0.1 , width = 8 , material = materials.wood)
wall3 = box(frame = eixoyellow ,pos = (20,-5,4), length = 30 , height = 0.1 , width = 8 , material = materials.wood)
symbol_yellow = cylinder(frame = eixoyellow, pos=(30,0,0.09), axis = (0,0,1), length= 0.01, radius = 4, color=color.yellow)

#EIXO.WHITE

eixowhite = frame()
wall1 = box(frame = eixowhite ,pos = (-35,0,4), length = 0.1 , height = 10 , width = 8 , material = materials.wood)
wall2 = box(frame = eixowhite ,pos = (-20,5,4), length = 30 , height = 0.1 , width = 8 , material = materials.wood)
wall3 = box(frame = eixowhite ,pos = (-20,-5,4), length = 30 , height = 0.1 , width = 8 , material = materials.wood)
symbol_white = cylinder(frame = eixowhite, pos=(-30,0,0.09), axis = (0,0,1), length= 0.01, radius = 4, color=color.white)

#COORDENADA

pointer = arrow(pos=(0,0,10),axis=(2,0,0),shafwidth=1,color=color.orange)
pointer2 = arrow(pos=(0,0,10),axis=(0,2,0),shafwidth=1,color=color.white)
pointer2 = arrow(pos=(0,0,10),axis=(0,0,2),shafwidth=1,color=color.green)

#ROBOT

robot = frame()
cyl= cylinder(frame=robot, pos=(0,0,0.495), axis=(0,0,0.7), length= 0.1, radius=2, color=color.red)
#rodas
wheell= cylinder(frame=robot, pos=(0,1.5,0.6), axis=(0,0.1,0), length= 0.3, radius=0.5, color=color.black)
wheel2= cylinder(frame=robot, pos=(0,-1.8,0.6), axis=(0,0.1,0), length= 0.3, radius=0.5, color=color.black)
#calota
cy1= cylinder(frame=robot, pos=(0,1.4995,0.6), axis=(0,0.1,0), length= 0.301, radius=0.3, color=color.white)
cy1= cylinder(frame=robot, pos=(0,-1.8005,0.6), axis=(0,0.1,0), length= 0.301, radius=0.3, color=color.white)
#Esfera
cyl= cylinder(frame=robot, pos=(1.8,0,0.295), axis=(0,0,0.1), length= 0.2, radius=0.2, color=color.black)
sph= sphere(frame=robot,pos=(1.8,0,0.3), radius=0.2, color=(192,192,192))
#MOTOR
motor1 = box(frame = robot ,pos = (0,1.3,0.7), length = 0.2 , height = 0.5 , width = 0.2 , material = materials.chrome)
motor2 = box(frame = robot ,pos = (0,-1.3,0.7), length = 0.2 , height = 0.5 , width = 0.2 , material = materials.chrome)
motor1 = box(frame = robot ,pos = (0,1.05,0.7), length = 0.205 , height = 0.05 , width = 0.205 , color=color.black)
motor1 = box(frame = robot ,pos = (0,-1.05,0.7), length = 0.205 , height = 0.05 , width = 0.205 , color=color.black)

########################################################################################################################

#TIME

time = 0
dt = 0.01
tmax = 200
time2 = 0
tmax2 = 50
dt2=1

velocity = [1,0,0]
posi0 = [0,0,0]
robot.velocity = vector(1,0,0)
theta = 0.001745


#  DISTRIBUICOES GAUSIANAS PARA CADA ESTACAO DE COR:

#  CADA VEZ QUE O CARRINHO ALCANCAR UMA ESTACAO - (ACTION)  ELE VAI RECEBER UMA RECOMPENSA 
#  QUE EH UM PROCESSO ALEATORIO, POREM PARA CADA TEMPO PASSADO NO AMBIENTE O CARRO VAI PERDER
#  SEUS PONTOS E TODA VEZ QUE CHEGAR NA BASE PERDE MAIS PONTO, O OBJETIVO EH ELE SOBREVIVER
#  A UM DIA DENTRO DESSE AMBIENTE.

#  OBJETIVO:
#  ELE DEVE APRENDER A LIDAR COM OS DADOS E DEDUZIR A PROBABILIDADE DOS VALORES DE CADA
#  COR E ESCOLHER A COR QUE OU LHE FORNECE A MELHOR MEDIA CONSTANTE DE VALOR OU UM CAMINHO
#  QUE LEVA A COLETA DE RECOMPENSAS ALTAS POREM COM MAIS TEMPO DE DEMORA











################  DEFINIR CONJUNTO DE AÇOES ###########################
def action_y (dt,time):
 robot.velocity = vector(1,0,0)
 #print(robot.axis.y)
 if(robot.axis.y <= 1):
    while time<9:
        rate(1000)
        time+=dt
        if(robot.axis.y >= -0.9999):
           robot.rotate(vector=robot.rotate,angle=theta,axis=(0,0,-1))
           #print(robot.axis.y)
 while time < 100: 
   rate(1000)
   time+=dt
   if(robot.pos.x >= symbol_yellow.pos.x):
      if(robot.axis.y <= 0):
         robot.rotate(vector=robot.rotate,angle=theta,axis=(0,0,-1))
      else:
         robot.velocity = vector(-1,0,0)
         robot.pos = robot.pos + robot.velocity*dt         
         if(robot.pos.x <= 0):
             robot.velocity = vector(0,0,0)
   else:
       robot.pos = robot.pos + robot.velocity*dt
       if(robot.pos.x <= 0):
          robot.velocity = vector(0,0,0)
# end def action_y

def action_w (velocidade=(-1,0,0)):
   robot.velocity = velocidade
   while time < tmax: 
              rate(1000)
              time+=dt
              if(robot.pos.x <= symbol_white.pos.x):
                if(robot.axis.y >= 0):
                 robot.rotate(vector=robot.rotate,angle=theta,axis=(0,0,1))
                else:
                 robot.velocity = vector(1,0,0)
                 robot.pos = robot.pos + robot.velocity*dt
                if(robot.pos.x >= 0):
                    robot.velocity = vector(0,0,0)
              else:
                robot.pos = robot.pos + robot.velocity*dt
                if(robot.pos.x >= 0):
                    robot.velocity = vector(0,0,0)
# end def action_w


def action_m (velocidade=(0,1,0)):
   robot.velocity = velocidade
   while time < tmax: 
              rate(1000)
              time+=dt
              if(robot.pos.y <= symbol_blue.pos.y):
                if(robot.axis.y <= 0):
                 robot.rotate(vector=robot.rotate,angle=theta,axis=(0,0,1))
                else:
                 robot.velocity = vector(0,1,0)
                 robot.pos = robot.pos + robot.velocity*dt
                if(robot.pos.y >= 0):
                    robot.velocity = vector(0,0,0)
              else:
                robot.pos = robot.pos + robot.velocity*dt
                if(robot.pos.y >= 0):
                    robot.velocity = vector(0,0,0)
# end def action_b

def action_b (dt,time):
   robot.velocity = vector(0,-1,0)
   print(robot.axis.y)
   if(robot.axis.y >= 0):
    while time<9:
        rate(1000)
        time+=dt
        if(robot.axis.y >= -1):
           robot.rotate(vector=robot.rotate,angle=theta,axis=(0,0,-1))
           #print(robot.axis.y)
        elif(robot.axis.y <= 0):
           robot.rotate(vector=robot.rotate,angle=theta,axis=(0,0,1))
           #print(robot.axis.y)
   while time < 100:              
              rate(1000)
              time+=dt
              if(robot.pos.y <= symbol_blue.pos.y):
                if(robot.axis.y <= 0.9999):
                 robot.rotate(vector=robot.rotate,angle=theta,axis=(0,0,1))
                 #print(robot.axis.y)
                else:
                 robot.velocity = vector(0,1,0)
                 #print(robot.axis.y)
                 robot.pos = robot.pos + robot.velocity*dt
                if(robot.pos.y >= 0):
                    robot.velocity = vector(0,0,0)
              else:
                robot.pos = robot.pos + robot.velocity*dt
                if(robot.pos.y >= 0):
                    robot.velocity = vector(0,0,0)
# end def action_b


while time < tmax:
    action_b(0.01,0)
    action_y(0.01,0)
    time+=dt
     
     


############################################################################################## BANANA ZEBRA ZEZO 

#RECEIVE WHICH COLOR YOU WANT TO GO TO
'''rightcolor = 0
color = raw_input('Enter the color you want to go to:')
while (rightcolor != 1): 
    if(color == 'yellow' or color == 'Yellow' or color == 'YELLOW'):
        rightcolor = 1
        robot.velocity = vector(1,0,0)
        while time < tmax: 
              rate(1000)
              time+=dt
              if(robot.pos.x >= symbol_yellow.pos.x):
                #robot.velocity = -1 * robot.velocity
                if(robot.axis.y >= 0):
                 robot.rotate(vector=robot.rotate,angle=theta,axis=(0,0,1))
                else:
                 robot.velocity = vector(-1,0,0)
                 robot.pos = robot.pos + robot.velocity*dt         
                if(robot.pos.x <= 0):
                    robot.velocity = vector(0,0,0)
              else:
                robot.pos = robot.pos + robot.velocity*dt
                if(robot.pos.x <= 0):
                    robot.velocity = vector(0,0,0)
                   # robot.axis.y = robot.axis.y + theta
              posi0 = robot.pos
    if(color == 'white' or color == 'White' or color == 'WHITE'):
        rightcolor = 1
        robot.velocity = vector(-1,0,0)
        while time < tmax: 
              rate(1000)
              time+=dt
              if(robot.pos.x <= symbol_white.pos.x):
                #robot.velocity = -1 * robot.velocity
                if(robot.axis.y >= 0):
                 robot.rotate(vector=robot.rotate,angle=theta,axis=(0,0,1))
                else:
                 print(robot.velocity)
                 robot.velocity = vector(1,0,0)
                 robot.pos = robot.pos + robot.velocity*dt
                 print(robot.velocity)
                          
                if(robot.pos.x >= 0):
                    robot.velocity = vector(0,0,0)
              else:
                robot.pos = robot.pos + robot.velocity*dt
                if(robot.pos.x >= 0):
                    robot.velocity = vector(0,0,0)
                    #robot.axis.y = robot.axis.y + theta
              posi0 = robot.pos
    else:
        color = raw_input('You choose poorly. Choose which color you want to go:')'''

  
