import numpy as np
from pylab import *
import matplotlib.pyplot as plt
import random as rd
import numpy as np
total = 0
area = 0
var = 0
loop = 0
diferencias = []
casos = []
def dist():
    return (rd.uniform(0,1)**2)+(rd.uniform(0,1)**2) 
while total<1400000:
    distancia = dist()
    if distancia<=1:
        area = area+1
    total = total+1
    var = var+1
    if var >= 200:
        pi = (area/total)*4
        diff=np.abs(3.14159265359-pi)
        diferencias.append(diff)
        var = 0
        loop = loop+200
        casos.append(loop)

fig = plt.figure()
ax =fig.add_subplot(111,title="Exactitud de pi")
ylim(0,0.05)
xlim(0,1400000)
ax.plot(casos,diferencias)
ax.set_xlabel("Número de casos (en millones)")
ax.set_ylabel("Diferencia con pi")
plt.show()
