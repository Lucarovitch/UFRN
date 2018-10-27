import math
from matplotlib import pyplot as plt
import numpy as np 
import random
NumberOfSteps = 0
Reward = []
OldEpsilon = 0.1
while(NumberOfSteps!= 100):
    Place = random.random()
    if (Place>= 0.75):
        ActualPlace = "Red"
        Reward.append(3)
      #  Reward = Reward + 1 #1 of reward in this place
    elif (Place >= 0.5 and Place < 0.75):
        ActualPlace = "Blue"
        Reward.append(2)
     #   Reward = Reward + 0 #No rewards in this place
    elif (Place >= 0.25 and Place < 0.5):
        ActualPlace = "Green"
        Reward.append(1)
      #  Reward = Reward + 0 #No rewards in this place
    elif (Place < 0.25):
        ActualPlace = "White"
        Reward.append(0)
      #  Reward = Reward + 0 #No rewards in this place
    
   #if (NumberOfSteps < 25):
    #    OldEpsilon.append(0.1)
    #elif (NumberOfSteps >= 25 and NumberOfSteps < 50):
     #   OldEpsilon.append(0.2)
    #elif (NumberOfSteps >= 50 and NumberOfSteps < 75):
     #   OldEpsilon.append(0.3)
    #elif (NumberOfSteps >= 75 and NumberOfSteps < 100):
     #   OldEpsilon.append(1)
    
    NewEpsilon = random.random()
    while (OldEpsilon>=NewEpsilon):
        if (max(Reward) == 0):
            ActualPlace = "White"
            Reward.append(0)
            #print(OldEpsilon[NumberOfSteps])
        elif (max(Reward) == 1):
            ActualPlace = "Green"
            Reward.append(1)
            #print(OldEpsilon[NumberOfSteps])
        elif (max(Reward) == 2):
            ActualPlace = "Blue"
            Reward.append(2)
            #print(OldEpsilon[NumberOfSteps])      
        elif (max(Reward) == 3):
            ActualPlace = "Red"
            Reward.append(3)
            #print(OldEpsilon[NumberOfSteps])
        NewEpsilon = random.random()
        NumberOfSteps+=1
        
    NumberOfSteps = NumberOfSteps + 1
    print(Reward)
    
    
