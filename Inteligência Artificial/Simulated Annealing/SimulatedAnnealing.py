
# coding: utf-8

# # Simulated Annealing em Python
# Disciplina: Inteligência Artificial Aplicada
# Professor: Sérgio Nathan
# Grupo: Ana Karoline;
# Jonathan Martins;
# Lucas Solano Cadengue;
# Rafael Dias;

# Primeiro iremos importar as bibliotecas e definir a função utilizada para obter o máximo.

# In[2]:


from matplotlib import pyplot as plt
import numpy as np 

def funcao(x):
	funcao = np.sin(15*x) + np.cos(5*x)
	return funcao

funcaovetorizada = np.vectorize(funcao)
x = np.linspace(-1, 1, num = 1000)
plt.plot(x, funcao(x))


# Agora nós vamos efetivamente fazer a função Simulated Annealing (SA)

# In[3]:


def SA(espacobusca, func, Temperatura):
    scale = np.sqrt(Temperatura)
    inicio = np.random.choice(espacobusca)
    x = inicio * 1
    atual = func(x)
    historico = [x]
    for i in range(1000):
        prop = x + np.random.normal()*scale # Adicionando o ruído
        if prop > 1 or prop < 0 or np.log(np.random.rand()) * Temperatura < (func(prop) - atual): # Para o problema da minimização
            prop = x
        x = prop
        atual = func(x)
        Temperatura = 0.8*Temperatura # Esfriando a temperatura em 20% por iteração
        historico.append(x) 
    return x, historico


# E agora nós vamos chamar a função e plotar os resultados (em uma cor nós temos a função e em outra o caminho que ele fez até chegar no máximo).

# In[4]:


x1, historico = SA(x, funcao, Temperatura = 4)
#print(SA(x,funcao,Temperatura = 4))
plt.plot(x, funcaovetorizada(x))
plt.scatter(x1, funcao(x1), marker = 'x')
plt.plot(historico, funcaovetorizada(historico))

plt.grid(False)
plt.show()
