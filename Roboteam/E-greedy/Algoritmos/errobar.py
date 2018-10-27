import math
from matplotlib import pyplot as plt
import numpy as np 
import random
import pylab as P
from scipy.stats import beta
import pandas as pd
from matplotlib.ticker import MaxNLocator
from collections import namedtuple



x = [0.028931723,0.1413269166,0.4103490503,0.8136918561,0.9250761028]
y1 = [0.2976190476,0.4033613445,0.369047619,0.2053571429,0.3165266106] #peixes
y2 =[0.29152148664343785,0.41173,0.43612078977932617,0.33101045296167214,0.28513] #algoritimo normal
y3 = [0.4443902439024389,0.7221951219512196,0.6423170731707316,0.37731707317073165,0.3071951219512195] #algoritimo com 100 iteracoes

y4=[0.7972195121951221,0.8573902439024388,0.6836097560975611,0.39168292682926825,0.30514634146341457]# 500 itera
desv4=[0.194848,0.03516607154268713,0.021860843766524956,0.022870727935763637,0.019680448358478014]

y5=[0.6390853658536584,0.7982317073170733,0.6664024390243903,0.3920731707317074,0.3034756097560975]
desv5=[0.1711,0.132076225107127,0.04248582539982974,0.03749757081166364,0.03670655740239766]

desv1 = [0.1385597006,0.2259507797,0.2001511145,0.1701173398,0.08237747115] #desvios dos peixes
desv2 = [0.4285,0.3858,0.23549,0.12109,0.1189] #algoritimo
desv3 = [0.4406,0.2113,0.07028,0.04535,0.05017]#desvio peixes 100 interacoes



'''
fig = P.figure()
P.errorbar(x, y3, desv1, fmt='o',ls='-',label='100 interactions')

plt.ylabel('Mean Value')
plt.xlabel('Epsilon')

fig = P.figure()
P.errorbar(x, y2, desv1, fmt='o',ls='-',label='21 interactions')
plt.ylabel('Mean Value')
plt.xlabel('Epsilon')
'''

'''
plt.figure()
plt.errorbar(x, y5, desv5, fmt='o',ms=12,capsize=10)
plt.ylabel('Average Reward', fontsize=24)
plt.xlabel('Epsilon', fontsize=24)
'''

'''ax = axs[1]
ax.errorbar(x, y2, desv2, fmt='--o')

plt.grid(True)

ax = axs[2]
ax.errorbar(x, y3, desv3, fmt='--o')
'''
fig, ax = plt.subplots()
K = 4
error_config = {'ecolor': '0.3'}
#index = (0,1.175,2.175,3.175,4.175)
#index3 = (0.35,1.52,2.52,3.52,4.52)
index = (0,1,2,3,4)
index3 = (0.35,1.35,2.35,3.35,4.35)
index2 = np.arange(K+2)
eplison_bar = (0.29152148664343785,0.41173,0.43612078977932617,0.33101045296167214,0.28513)
fish_bar = (0.2976190476,0.4033613445,0.369047619,0.2053571429,0.3165266106)
std_ep = (0.34/2,0.394/2,0.264/2,0.25198/2,0.150/2)
std_peixe=(0.1385597006,0.2259507797,0.2001511145,0.1701173398,0.08237747115)

bar_width = 0.35

rects1 = ax.bar(index,eplison_bar, bar_width,alpha=0.5,
                 color='g',yerr=std_ep,error_kw=error_config,
                label=r'$\epsilon$-greedy')
rects2 = ax.bar(index3,fish_bar, bar_width,alpha=0.5,
                 color='r',yerr=std_peixe,error_kw=error_config,
                label='Experimental value')

ax.plot([0,1,2,3,4], [0.29152148664343785,0.41173,0.43612078977932617,0.33101045296167214,0.28513], 'o')
ax.plot([0.35,1.35,2.35,3.35,4.35], [0.2976190476,0.4033613445,0.369047619,0.2053571429,0.3165266106], 'o')
#legend = ax.legend(loc='right', shadow=True, fontsize='xx-large')
#legend.get_frame().set_facecolor('#00FFCC')
ax.set_xticks(index2 + bar_width / 2)
ax.set_xticklabels((' 0.0289 ', ' 0.1413', ' 0.4103 ', ' 0.8137 ' , ' 0.925 '))
fig.tight_layout()
ax.set_xlabel(r'$\epsilon$, Normalized Cortisol Level',fontsize=24)
ax.set_ylabel('Total Reward',fontsize=24)
ax.set_ylim([0.00,1.00])
ax.legend(fontsize=45)

plt.legend()
plt.grid(False)
plt.show()


