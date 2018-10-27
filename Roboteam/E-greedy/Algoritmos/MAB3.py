import math
from matplotlib import pyplot as plt
import numpy as np 
import random

random.seed()

mudar = 21
sam=0
vector=[]
Mean_Reward = 0.0
while(sam<82):
 #vector.append(float(Mean_Reward))
 NumberOfSteps = 1
 Reward = []
 OldEpsilon = float(0.1413)       #
 Place = random.random()
 Mean_Reward = 0.00
 #print("Place", Place)
 if (Place>= 0.75):
    ActualPlace = "Red"
    Reward.append(1)
#  Reward = Reward + 1 #1 of reward in this place
 elif (Place >= 0.5 and Place < 0.75):
    ActualPlace = "Blue"
    Reward.append(0)
#   Reward = Reward + 0 #No rewards in this place
 elif (Place >= 0.25 and Place < 0.5):
    ActualPlace = "Green"
    Reward.append(0)
# Reward = Reward + 0 #No rewards in this place
 elif (Place < 0.25):
    ActualPlace = "White"
    Reward.append(0)
#  Reward = Reward + 0 #No rewards in this place
 while(NumberOfSteps!= mudar):    
    NewEpsilon = random.random()
    #print("Epsilon", NewEpsilon)
    if (OldEpsilon<=NewEpsilon):
        if (max(Reward) == 0):
            Place = random.random()
            if(Place >= 0.66):
                ActualPlace = "Blue"
            elif (Place >= 0.33 and Place < 0.66):
                ActualPlace = "Green"
            elif (Place < 0.33):
                ActualPlace = "White"
            Reward.append(0)
            #print(OldEpsilon[NumberOfSteps])
        elif (max(Reward) == 1):
            ActualPlace = "Red"
            Reward.append(1)
            #print(OldEpsilon[NumberOfSteps])
       # elif (max(Reward) == 2):
       #     ActualPlace = "Blue"
       #     Reward.append(2)
            #print(OldEpsilon[NumberOfSteps])      
       # elif (max(Reward) == 3):
       #     ActualPlace = "Red"
        #    Reward.append(3)
        #    #print(OldEpsilon[NumberOfSteps])
    else:           
        Place = random.random()
        #print("Place", Place)
        if (Place>= 0.75):
             ActualPlace = "Red"
             Reward.append(1)
         #  Reward = Reward + 1 #1 of reward in this place
        elif (Place >= 0.5 and Place < 0.75):
            ActualPlace = "Blue"
            Reward.append(0)
        #   Reward = Reward + 0 #No rewards in this place
        elif (Place >= 0.25 and Place < 0.5):
            ActualPlace = "Green"
            Reward.append(0)
            #  Reward = Reward + 0 #No rewards in this place
        elif (Place < 0.25):
            ActualPlace = "White"
            Reward.append(0)
        #  Reward = Reward + 0 #No rewards in this place
    NumberOfSteps = NumberOfSteps + 1
    Sum_Reward = sum(Reward)
    #print("Somatorio Recompensas", Sum_Reward)
    Mean_Reward = ((float(Sum_Reward)) / (float(NumberOfSteps)))
    #print("Media", Mean_Reward)
    #print(Reward)
 sam+=1
 vector.append(float(Mean_Reward))

print("vetora ai =",vector)
k=0
o=sam-1
md=0
for k in range(o+1):
  md = vector[k] + md
  #print("oia=",vector[k],"k=",k)
md=md/(o+1)
######### 1 media ################
print("media1=",md)
desv = 0
for k in range(o+1):
    desv = desv + (float(vector[k] - md))**2
desv = desv / (o+1)
desv = math.sqrt(desv)
print("desvio=",desv)

########################################
