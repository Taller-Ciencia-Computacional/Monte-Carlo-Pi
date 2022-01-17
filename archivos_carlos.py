import random as rd
import numpy as np
import matplotlib as plt

def distance():
    if np.sqrt(rd.uniform(0, 1)**2+rd.uniform(0, 1)**2) <=1:
        return 1
    else:
        return 0

num = 10000
ins = 0

for a in range(num):
    ins = ins + distance()

print ("pi was approximated at::", ins/num*4)

try:
    with open("pi_approximation.txt" , "w") as f:
        f.write("ins/num*4")
except:
    with open("pi_approximation.txt" , "w+") as f:
        f.write("ins/num*4")

