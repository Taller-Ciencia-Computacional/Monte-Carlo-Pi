import random as rd
import numpy as np
import matplotlib.pyplot as plt


ins = 0
y = []
x = np.linspace(0, 1000000, 100000)


def distance():
    if np.sqrt((rd.uniform(0, 1)**2)+ rd.uniform(0, 1)**2) <= 1:
        return 1
    else:
        return 0
    
num = 0
for i in range(100000):
    for i in range(10):
        ins = ins + distance()
    num = num + 10
    y.append(ins*4/num)


fig = plt.figure(dpi = 100)
ax = fig.add_subplot(111)
ax.plot(x, y)
plt.show()
