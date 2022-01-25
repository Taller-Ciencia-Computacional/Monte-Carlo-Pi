import random
import numpy as np
import matplotlib.pyplot as pyplot

pi = 0
file_opened = 0
alist = []

def files():
    global file
    global file_opened
    global file_name
    
    if file_opened == 0:
        file_name = input("Enter file name: ")
        file_name = file_name + ".txt"
        try:
            file = open(file_name, "a")
            file_opened = 1
        except:
            print("No such file exists.")
            

def distance():
    x = random.uniform(0, 1)
    y = random.uniform(0, 1)
    if np. sqrt(x**2 + y**2) <= 1:
        return 1
    else:
        return 0

def algorithm():
    global pi
    
    number = 100000
    in_area = 0
    for i in range(number):
        in_area = in_area + distance()

    pi = (in_area / number) * 4
    print(pi)

def pi_store():
    global pi
    global file
    global pi_txt
    
    if pi == 0:
        print("Empty variable.")
    else:
        pi_txt = str(pi) + "\n"
        file.write(pi_txt)

def average():
    global alist
    global file
    global pi_txt
    global file_name
    
    file.close()
    file = open(file_name, "r")
    for aline in file:
        # Fix
        values = aline.split()
        alist = alist + values
    print(values)
    

def App():
    choices = ["0", "1", "2", "3"]
    choice = ""
    while choice not in choices:
        print("MonteCarlo Algorithm")
        print("1. Perform the algorithm")
        print("2. Store variable in file")
        print("3. Perform an average")
        print("0. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            algorithm()
        if choice == "2":
            files()
            pi_store()
        if choice == "3":
            files()
            average()
        if choice == "0":
            if file_opened == 1:
                file.close()
            exit()
        choice = ""

App()
        
