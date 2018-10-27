
# coding: utf-8

# # Simulated Annealing em Python
# Disciplina: Inteligência Artificial Aplicada
# Professor: Sérgio Nathan
# Grupo: Ana Karoline;
# Jonathan Martins;
# Lucas Solano Cadengue;
# Rafael Dias;

# Primeiro iremos importar as bibliotecas e definir a função utilizada para obter o mínimo.

from matplotlib import pyplot as plt
import numpy as np 
import math

def funcao(x1,x2,x3,x4,x5):
	funcao = 50 + x1**2 - 10*np.cos(2*math.pi*x1) + x2**2 - 10*np.cos(2*math.pi*x2) + x3**2 - 10*np.cos(2*math.pi*x3) + x4**2 - 10*np.cos(2*math.pi*x4) + x5**2 - 10*np.cos(2*math.pi*x5) 
	return funcao

funcaovetorizada = np.vectorize(funcao)
x1 = np.linspace(-1, 1, num = 1000000)
x2 = np.linspace(-1, 1, num = 1000000)
x3 = np.linspace(-1, 1, num = 1000000)
x4 = np.linspace(-1, 1, num = 1000000)
x5 = np.linspace(-1, 1, num = 1000000)


# Agora nós vamos efetivamente fazer a função Simulated Annealing (SA)

def SA(espacobusca1, espacobusca2, espacobusca3, espacobusca4, espacobusca5, func, Temperatura):
    scale = np.sqrt(Temperatura) #Para ajudar a escolher o vizinho
    # Escolhendo os pontos de partida
    inicio1 = np.random.choice(espacobusca1)
    inicio2 = np.random.choice(espacobusca2)
    inicio3 = np.random.choice(espacobusca3)
    inicio4 = np.random.choice(espacobusca4)
    inicio5 = np.random.choice(espacobusca5)
    x1 = inicio1 * 1
    x2 = inicio2 * 1
    x3 = inicio3 * 1
    x4 = inicio4 * 1
    x5 = inicio5 * 1
    atual = func(x1,x2,x3,x4,x5)
    while Temperatura > 0.0000000000000000000000000000001:
        prop1 = x1 + np.random.normal()*scale # Adicionando o ruído e escolhendo o vizinho
        prop2 = x2 + np.random.normal()*scale
        prop3 = x3 + np.random.normal()*scale 
        prop4 = x4 + np.random.normal()*scale
        prop5 = x5 + np.random.normal()*scale 
        # Verificando as propostas
        # Para o problema da minimização
        if prop1 > 1 or prop1 < 0 or np.log(np.random.rand()) * Temperatura < 	1-np.e**-(func(prop1,prop2,prop3,prop4,prop5) - atual): 
            prop1 = x1
        x1 = prop1

        if prop2 > 1 or prop2 < 0 or np.log(np.random.rand()) * Temperatura < 1-np.e**-(func(prop1,prop2,prop3,prop4,prop5) - atual): 
            prop2 = x2
        x2 = prop2

        if prop3 > 1 or prop3 < 0 or np.log(np.random.rand()) * Temperatura < 1-np.e**-(func(prop1,prop2,prop3,prop4,prop5) - atual): 
            prop3 = x3
        x3 = prop3

        if prop4 > 1 or prop4 < 0 or np.log(np.random.rand()) * Temperatura < 1-np.e**-(func(prop1,prop2,prop3,prop4,prop5) - atual):
            prop4 = x4
        x4 = prop4

        if prop5 > 1 or prop5 < 0 or np.log(np.random.rand()) * Temperatura < 1-np.e**-(func(prop1,prop2,prop3,prop4,prop5) - atual): 
            prop5 = x5
        x5 = prop5

        atual = func(x1,x2,x3,x4,x5)
        Temperatura = 0.9999*Temperatura # Esfriando a temperatura em 0.0001% a cada iteração
    return x1, x2, x3, x4, x5, funcao(x1,x2,x3,x4,x5)


# E agora nós vamos chamar a função e printar os resultados.

# In[4]:


x1, x2, x3, x4, x5, valorfuncao = SA(x1, x2, x3, x4,x5, funcao, Temperatura = 4)
print("x1: ", x1)
print("x2: ", x2)
print("x3: ", x3)
print("x4: ", x4)
print("x5: ", x5)
print("Valor da funcao: ", valorfuncao)

