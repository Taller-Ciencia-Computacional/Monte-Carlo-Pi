import numpy as np
import random as rd
from pylab import *
import matplotlib.pyplot as plt
total = 0
area = 0
def dist():
    return (rd.uniform(0,1)**2)+(rd.uniform(0,1)**2) 
while total<100:
    distancia = dist()
    if distancia<=1:
        area = area+1
    total = total+1
pi = (area/total)*4
n1 = pi
total = 0
area = 0
while total<400:
    distancia = dist()
    if distancia<=1:
        area = area+1
    total = total+1
pi = (area/total)*4
n2 = pi
total = 0
area = 0
while total<1600:
    distancia = dist()
    if distancia<=1:
        area = area+1
    total = total+1
pi = (area/total)*4
n3 = pi
total = 0
area = 0
while total<6400:
    distancia = dist()
    if distancia<=1:
        area = area+1
    total = total+1
pi = (area/total)*4
n4 = pi
total = 0
area = 0
while total<25600:
    distancia = dist()
    if distancia<=1:
        area = area+1
    total = total+1
pi = (area/total)*4
n5 = pi
total = 0
area = 0

d1 = 3.14159265359-n1
diff1 = abs(d1)
d2 = 3.14159265359-n2
diff2 = abs(d2)
d3 = 3.14159265359-n3
diff3 = abs(d3)
d4 = 3.14159265359-n4
diff4 = abs(d4)
d5 = 3.14159265359-n5
diff5 = abs(d5)
diferencias = [diff1,diff2,diff3,diff4,diff5]
casos = [100,400,1600,6400,25600]
print(diferencias)
fig = plt.figure()
ax =fig.add_subplot(111,title="Exactitud de pi")
ax.plot(casos,diferencias)
ax.set_xlabel("Número de casos")
ax.set_ylabel("Diferencia con pi")
plt.show()
