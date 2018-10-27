from matplotlib import pyplot as plt
import numpy as np 
import math

def funcao(x1,x2,x3,x4,x5):
	funcao = 50 + x1**2 - 10*np.cos(2*math.pi*x1) + x2**2 - 10*np.cos(2*math.pi*x2) + x3**2 - 10*np.cos(2*math.pi*x3) + x4**2 - 10*np.cos(2*math.pi*x4) + x5**2 - 10*np.cos(2*math.pi*x5) 
	#funcao = 50 + x1**2 - 10*np.cos(2*math.pi*x1)
	return funcao

print(funcao(0,0,0,0,0))