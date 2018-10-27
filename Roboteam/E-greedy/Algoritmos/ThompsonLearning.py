from visual import *
from visual.graph import * # graphing capability
import math
from matplotlib import pyplot as plt
import random
from random import randint
import numpy as np
from scipy.special import gamma  # usando gamma
import pylab
from scipy.stats import beta
import panda as pd
from matplotlib.ticker import MaxNLocator
from collections import namedtuple

fig, ax = plt.subplots(1,1)

# Função de distribuição Beta:

def beta_pdff(x,a,b):
    return float( gamma(a+b)/(gamma(a)*gamma(b)) ) *(x**(a-1)) * ((1-x)**(b-1))
def gauss_pdf(x, mu, sigma):
    return (1./(math.sqrt(2.*math.pi)*sigma))*math.exp(-np.power((x - mu)/sigma, 2.)/2)

a, b = 2.0,1.0
#x = np.linspace(beta.ppf(0.01, a, b),beta.ppf(0.99, a, b), 100)
y = np.linspace(0, 1, 1002)[1:-1]

#ax.plot(x, beta.pdf(x, a, b),'r-', lw=5, alpha=0.6, label='beta pdf')
'''
dis = beta(a,b)
dis2 = beta(a+1.,b)
dis3 = beta(a+2.,b)
dis4 = beta(a+2.,b+1.)
dis5 = beta(a+8.,b+2.)
dis6 = beta(a+10.,b+6.)
dis7 = beta(a+20.,b)
ax.plot(y,dis.pdf(y),'r-', lw=1, alpha=0.6, label='a=2.0 b=1.0')
ax.plot(y,dis2.pdf(y),'b-', lw=1, alpha=0.6,  label='a=3.0 b=1.0')
ax.plot(y,dis3.pdf(y),'g-', lw=1, alpha=0.6,  label='a=3.0 b=2.0')
ax.plot(y,dis4.pdf(y),'b-', lw=1, alpha=0.6,  label='a=4.0 b=2.0')
ax.plot(y,dis5.pdf(y),'w-', lw=1, alpha=0.6,  label='a=10.0 b=3.0')
ax.plot(y,dis6.pdf(y),'k-', lw=1, alpha=0.6,  label='a=12.0 b=7.0')
ax.plot(y,dis7.pdf(y),'k--', lw=1, alpha=0.6,  label='a=22.0 b=0.0')
legend = ax.legend(loc='upper center', shadow=True, fontsize='x-large')
'''
#### Função do reward deterministica:

def recompensa(Place):
 if (Place == 0):
    #ActualPlace = "A"
    return 1
 elif (Place == 1):
    #ActualPlace = "B"
    return 0
 elif (Place == 2):
    #ActualPlace = "C"
    return 0
 elif (Place == 3):
    #ActualPlace = "D"
    return 0

def recompensa_gauss(Place):     
 if (Place == 0):
    #ActualPlace = "A"
    return  random.gauss(3,0.4)
 elif (Place == 1):
    #ActualPlace = "B"
    return  random.gauss(1,1)
 elif (Place == 2):
    #ActualPlace = "C"
    return  random.gauss(4,0.6)
 elif (Place == 3):
    #ActualPlace = "D"
    return  random.gauss(2,0.1)   


###############################################################

# Thompsons Learning for Beta distribution:

K = 4              # arms = 4
T = 100            # Period
S = [0] * K        # Sucess vector
F = [0] * K        # Failure vector
ad_vector = []     # Vetor î
total_reward = 0   # Somatorio das recompensas
recompensas_vector = []
prob_distr_0 = []
prob_distr_1 = []
prob_distr_2 = []
prob_distr_3 = []


for t in range(T):
  teta_max = 0
  ad = 0
  for i in range (K):
      teta_random = random.betavariate(S[i]+1,F[i]+1)
      if(i==0): 
       prob_distr_0.append(1./(1.+(F[0]+1.)/(S[0]+1.)))   
       #print(1/(1+(F[0]+1.)/(S[0]+1.)))
      elif(i==1):
       prob_distr_1.append(1./(1.+(F[1]+1.)/(S[1]+1.)))
      elif(i==2):
       prob_distr_2.append(1./(1.+(F[2]+1.)/(S[2]+1.)))
      elif(i==3):
       prob_distr_3.append( 1./( 1. + (F[3]+1.)/(S[3]+1.) ) )   
      if(teta_random > teta_max):
          teta_max = teta_random
          ad = i
  ad_vector.append(ad)
  #print("valor do indice i(arm)=",ad)
  #print("valor do teta max=",teta_max)
  reward = recompensa(ad)   #recebe reward de alguma function deterministico
  # mude recompensa para recompensa_gauss para obter processo estocastico
  if(reward == 1):          # mude seu parametro de seleção paravalores > 3
      S[ad] = S[ad] + 1     # por exemplo, e valores <=3 para recompensas
  elif(reward == 0):        # ruins
       F[ad] = F[ad] + 1
  recompensas_vector.append(total_reward + reward)
  total_reward = total_reward + reward
  #print(total_reward, t)


################################################################

# EM learning problem based on Thompson Sampling:

K = 4              # arms = 4
T1 = 3            # Period
S = [0]*K
F = [0]*K
Q = [0]*K          # vetor de cada arm  
P = [0.5]*K        # vetor de prior
Mu = [1,1,1,1]         # vetor de medias
Sigma = [0.1,0.1,0.1,0.1]      # vetor de variancia
X = []            # Vetores de dados -
total_reward_EM = 0         # Somatorio das recompensas
recompensas_vector_EM = []
ad_vector_EM = []

for t in range(T1):
  teta_max = 0
  ad = 0
  print("-------NEW Interaction---------")
  for i in range(K):
    teta_random = random.gauss(Mu[i],Sigma[i])
    print("arm=",i,"valor=",teta_random)
    if(teta_random > teta_max):
      teta_max = teta_random
      ad = i
  ad_vector_EM.append(ad)
  reward = recompensa(ad)
  X.append(reward)
  if(reward == 1):
      S[i] = S[i] + 1      
  else:
      F[i] = F[i] + 1
  P[i] = random.betavariate(S[i]+1,F[i]+1)
  print("P[",i,"]=",P[i])
  print("X =",X)
  total_reward_EM = total_reward_EM + reward
  recompensas_vector_EM.append(total_reward + reward)
  print("total rewards=",total_reward_EM)
  print("Mu[0],Sigma[0]=",Mu[0],Sigma[0])
  print("Mu[1],Sigma[1]=",Mu[1],Sigma[1])
  print("Mu[2],Sigma[2]=",Mu[2],Sigma[2])
  print("Mu[3],Sigma[3]=",Mu[3],Sigma[3])
##### EM STEP:
  # E-STEP:
  P_D1 = [0]*len(X)
  P_D2 = [0]*len(X)
  P_D3 = [0]*len(X)
  P_D4 = [0]*len(X)
  a=[0]*len(X)
  b=[0]*len(X)
  c=[0]*len(X)
  d=[0]*len(X)
  # Prior vector
  for j in range(len(X)):
   a[j] =  float(P[0]*gauss_pdf(X[j],Mu[0],Sigma[0])) + float(P[0]*gauss_pdf(X[j],Mu[1],Sigma[1])) + float(P[0]*gauss_pdf(X[j],Mu[2],Sigma[2])) + float(P[0]*gauss_pdf(X[j],Mu[3],Sigma[3])) 
  for j in range(len(X)):
   b[j] = float(P[1]*gauss_pdf(X[j],Mu[0],Sigma[0])) + float(P[1]*gauss_pdf(X[j],Mu[1],Sigma[1])) + float(P[1]*gauss_pdf(X[j],Mu[2],Sigma[2])) + float(P[1]*gauss_pdf(X[j],Mu[3],Sigma[3])) 
  for j in range(len(X)):
   c[j] =float(P[2]*gauss_pdf(X[j],Mu[0],Sigma[0]))+ float(P[2]*gauss_pdf(X[j],Mu[1],Sigma[1]))+ float(P[2]*gauss_pdf(X[j],Mu[2],Sigma[2]))+ float(P[2]*gauss_pdf(X[j],Mu[3],Sigma[3])) 
  for j in range(len(X)):
   d[j] =float(P[3]*gauss_pdf(X[j],Mu[0],Sigma[0]))+ float(P[3]*gauss_pdf(X[j],Mu[1],Sigma[1]))+ float(P[3]*gauss_pdf(X[j],Mu[2],Sigma[2]))+ float(P[3]*gauss_pdf(X[j],Mu[3],Sigma[3])) 
  # Baysian vector
  for j in range(len(X)):
   P_D1[j]=float( P[0]*gauss_pdf(X[j],Mu[0],Sigma[0])/ float(a[j]) )
  for j in range(len(X)):
   P_D2[j]=float( P[1]*gauss_pdf(X[j],Mu[1],Sigma[1]) / float(b[j]))
  for j in range(len(X)):
   P_D3[j]=float( P[2]*gauss_pdf(X[j],Mu[2],Sigma[2]) / float(c[j]) )
  for j in range(len(X)):
   P_D4[j]=float( P[3]*gauss_pdf(X[j],Mu[3],Sigma[3]) / float(d[j]) )
  print("PD1=",P_D1)
  print("PD2=",P_D2)
  print("PD3=",P_D3)
  print("PD4=",P_D4)
  #M-STEP:
  mu = 0.
  sig = 0.
  for j in range(len(X)):
    mu = mu + P_D1[j] 
  mu = float(mu)/len(X)
  Mu[0] = mu
  for j in range(len(X)):
    sig = sig + ( (X[j]-mu)**2 ) * P_D1[j]  
  sig = float(sig)/len(X)
  Sigma[0]=sig
  # ARM 2 new feature vector
  mu = 0.
  sig = 0.
  for j in range(len(X)):
    mu = mu +  P_D2[j] 
  mu = float(mu)/len(X)
  Mu[1] = mu
  for j in range(len(X)):
    sig = sig + ( (X[j]-mu)**2 ) * P_D2[j]
  sig = float(sig)/len(X)
  Sigma[1]=sig  
  # ARM 3 new feature vector
  mu = 0.
  sig = 0.
  for j in range(len(X)):
    mu = mu +  P_D3[j] 
  mu = float(mu)/len(X)
  Mu[2] = mu
  for j in range(len(X)):
    sig = sig + ( (X[j]-mu)**2 ) * P_D3[j]  
  sig = float(sig)/len(X)
  Sigma[2]=sig
  # ARM 4 new feature vector
  mu = 0.
  sig = 0.
  for j in range(len(X)):
    mu = mu +  P_D4[j] 
  mu = float(mu)/sum(P_D1)
  Mu[3] = mu
  for j in range(len(X)):
    sig = sig + ( (X[j]-mu)**2 ) * P_D4[j] 
  sig = float(sig)/len(X)
  Sigma[3]=sig

  
#################################################################


def eplsion_greedy(epislon,T):
 K = 4
 Q = [0]*K    
 N = [0]*K
 Reward = []
 #T = 100
 total_reward_eg = 0
 for t in range(T):
   maior = 0
   ad = 0
   probability = random.random()
   if(probability > epislon):
    for i in range (K):
     if(Q[i] >= maior):  
        maior = Q[i]
        ad = i
   else:
    ad = randint(0,3)
   N[ad] = N[ad] + 1
   rewa = recompensa(ad)
   #Q[ad] = Q[ad] + (1/N[ad])*(rewa - Q[ad])
   Q[ad] = Q[ad] + rewa
   total_reward_eg = total_reward_eg + rewa
   Reward.append(total_reward_eg)
 return(Reward)

'''
def  eplsion_greedy(eplison,T):
 Reward_vector = []
 arm_vector = [0]*K
 Rew = []
 total_reward_MAB = 0
 total_vector = []
 OldEpsilon = eplison
 arm = randint(0,3)
 Rew.append(recompensa(arm))
 for t in range(T):
  NewEpsilon = random.random()
  if(NewEpsilon > OldEpsilon):
      Rew.append(max(Rew))
      arm = 1
  else:
      arm = randint(0,3)
      Rew.append(recompensa(arm))
  total_reward_MAB = sum(Rew)
  total_vector.append(total_reward_MAB)
  arm_vector[arm]=arm_vector[arm] + 1
 return(sum(Rew))
'''
def eplsion_trials(trials,eplsion,T):
 t=0
 media_recompensa=[]
 while(t<trials):
   media_recompensa.append(eplsion_greedy(eplsion,T))  
   t+=1
 return(sum(media_recompensa)/trials)

def eplsion_var(trials,eplsion,T):
 t=0
 var = []
 media_recompensa=[]
 while(t<trials):
   media_recompensa.append(eplsion_greedy(eplsion,T))  
   t+=1
 md = sum(media_recompensa)/float(trials)
 #print("media=",md)
 for i in range(trials):
     var.append((eplsion_greedy(eplsion,T)-md)**2)
 variancia = sqrt(sum(var)/float(trials))
 return variancia

################################################################
# Epsilon Greedy -A simple bandit algorithm

K = 4
Q = [0]*K    
N = [0]*K
Reward_EG = []
epislon = 0.5
total_reward_eg = 0
prob_arm1_Eps = []
prob_arm2_Eps = []
prob_arm3_Eps = []
prob_arm4_Eps = []
ad1 = 0
ad0 = 0
ad2 = 0
ad3 = 0
for t in range(T):
  maior = 0
  ad = 0
  probability = random.random()
  if(probability > epislon):
   for i in range (K):
     if(Q[i] >= maior):  
      maior = Q[i]
      ad = i
  else:      
    ad = randint(0,3) 
  #print("indice=",ad)
  N[ad] = N[ad] + 1  
  rewa = recompensa(ad)
  #Q[ad] = Q[ad] + (1/N[ad])*(rewa - Q[ad])
  Q[ad] = Q[ad] + rewa 
  total_reward_eg = total_reward_eg + rewa
  Reward_EG.append(total_reward_eg)



################################################################

###### Plot graficos:

time = np.linspace(0, T, T)


fig, ax = plt.subplots()

# GRAFICOS DE RECOMPENSA
'''
cont = 0
Max_rew = []
for t in range(T):
   cont = cont + 1 
   Max_rew.append(cont)

#ax.plot(time,Max_rew, 'g', label='Max reward')
a1=eplsion_greedy(0.0289)
a2=eplsion_greedy(0.1413)
a3=eplsion_greedy(0.4103)
a4=eplsion_greedy(0.9250)
a5=eplsion_greedy(0.8137)
ax.plot(time,a1, 'g-', label=r'$\epsilon$-greedy = 0.0289')
ax.plot(time,a2, 'b-', label=r'$\epsilon$-greedy =0.1413')
ax.plot(time,a3, 'k-', label=r'$\epsilon$-greedy =0.4103 ')
ax.plot(time,a4, 'c-', label=r'$\epsilon$-greedy =0.9250 ')
ax.plot(time,a5, 'm-', label=r'$\epsilon$-greedy =0.8137')
print("epsilon 0.0289 = ",a1)
print("epsilon 0.1413 = ",a2)
print("epsilon 0.4103 = ",a3)
print("epsilon 0.9250 = ",a4)
print("epsilon 0.8137 = ",a5)
ax.plot(time, recompensas_vector, 'r', label='Thompson sampling')
legend = ax.legend(loc='upper left', shadow=True, fontsize='medium')
ax.set_xlabel('Time',fontsize=24)
ax.set_ylabel('Rewards',fontsize=24)
legend.get_frame().set_facecolor('#00FFCC')

'''
# GRAFICOS DE BARRA SUCESSO E FAIL:
'''
index = (0,1.175,2.175,3.175)
index3 = (0.35,1.35,2.35,3.35)
index2 = np.arange(K)
action_bar = (S[0],S[1],S[2],S[3])
fail_bar =(F[0],F[1],F[2],F[3])
print(arm_vector)
arm_bar = (arm_vector[0],arm_vector[1],arm_vector[2],arm_vector[3])
bar_width = 0.35
rects1 = ax.bar(index,action_bar, bar_width,alpha=0.4,
                 color='b',
                label='Sucess')
rects1 = ax.bar(index,fail_bar, bar_width,alpha=0.4,
                 color='r',
                label='Fail')
rects1 = ax.bar(index3,arm_bar, bar_width,
                 color='g',
                label='MAB-arm')
ax.set_xticks(index2 + bar_width / 2)
ax.set_xticklabels((' A ', ' B ', ' C ', ' D '))
fig.tight_layout()
ax.set_xlabel('Arms')
ax.set_ylabel('Number of choices')
ax.legend()
'''

# GRAFICO DE BARRAS DE SOMA DE RECOMPENSAS:
'''
index = (0.175,1.175,2.175,3.175,4.175)
index2 = np.arange(K+2)
index3 = (0.35,1.52,2.52,3.52,4.52)
error_config = {'ecolor': '0.3'}
std_ep = (100*0.1711,100*0.132076225107127,100*0.04248582539982974,100*0.03749757081166364,100*0.03670655740239766)
#a1 = eplsion_trials(81, 0.0289,100)
#a2 = eplsion_trials(81,0.1413,100)
#a3 = eplsion_trials(81, 0.4103,100)
#a4 = eplsion_trials(81, 0.8137,100)
#a5 = eplsion_trials(81,0.9250,100)



###
a1=27
a2=64
a3=61
a4=37
a5=29
eplison_bar = (27, 64, 61, 37, 29)
TS_bar = (total_reward,total_reward,total_reward,total_reward,total_reward)
vear_bar = (eplsion_var(21, 0.0289,82),eplsion_var(21,0.1413,82),eplsion_var(21,0.4103,82),eplsion_var(21,0.8137,82),eplsion_var(21,0.9250,82))
print("desvio padrao=",vear_bar)
bar_width = 0.35
print("vetor de media=",eplison_bar)
rects1 = ax.bar(index,eplison_bar, bar_width,alpha=0.8,
                color='g',yerr=std_ep,error_kw=error_config,label=r'$\epsilon$')
              
#rects2 = ax.bar(index3,TS_bar, bar_width,alpha=0.35,
                # color='r',
                #label='Thompson sampling')

ax.plot([0.175,1.175,2.175,3.175,4.175], [a1,a2,a3,a4,a5], 'o')
ax.set_xticks(index2 + bar_width / 2)
ax.set_xticklabels((' 0.0289 ', ' 0.1413 ', ' 0.4103 ', ' 0.8137 ' , ' 0.925 '))
fig.tight_layout()
ax.set_xlabel(r'$\epsilon$',fontsize=24)
ax.set_ylabel('Average Reward',fontsize=24)
ax.legend(fontsize=25)
'''
# GRAFICO DE PROBABILIDADE DO THOMPSON E GREEDY:


#fig,ax =plt. subplots()
'''
prob_distr_0 
ax.plot(time,prob_distr_0, 'r', label='Probability arm 0')
ax.plot(time, prob_distr_1,'g', label='Probability arm 1')
ax.plot(time, prob_distr_2,'b', label='Probability arm 2')
ax.plot(time, prob_distr_3,'k', label='Probability arm 3')
legend = ax.legend(loc='center right', shadow=True, fontsize='x-large')
ax.set_xlabel('Steps',fontsize=24)
ax.set_ylabel('Probability',fontsize=24)
legend.get_frame().set_facecolor('#00FFCC')
#plt.title("Thompson sampling Probability")
'''
####### ATIVANDO GRAFICOS ##########

#plt.grid(True)
#plt.title("Thompson sampling vs MAB")
plt.show()  


######  ATIVANDO GRAFICO DINAMICO #######
'''
graph3 = gdisplay(x=1000, y=100, width=400, height=300,
title='Phase Space', xtitle='angle (rad)', ytitle='omega (rad/s)',
foreground=color.black, background=color.white)
curve3 = gcurve(gdisplay = graph3, color = color.blue)
#curve3.plot(pos = (time, theta))
'''






    
