from tkinter import Label
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from scipy import optimize
from scipy.optimize import curve_fit
import csv

# 1.del 
vhod = []
ch1 = []
ch2 = []
ch3 = []
ch4 = []

meritve_1 = ["1_0000.csv", "1_0150.csv", "1_0330_M.csv", "1_0560.csv", "1_0820.csv"]
for i, el in enumerate(meritve_1):
    vhod_v = []
    ch1_v = []
    ch2_v = []
    ch3_v = []
    ch4_v = []
    with open(el, "r") as file:
        csvreader = csv.reader(file)
        for line in csvreader:
            print(line)
    


"""# 2. del - 
mer_2 = ["2_1.dat", "2_3.txt"]
meritve_2 = []
for el in mer_2:
    U = []
    fre = []
    mer = open(el, "r")
    for line in mer:
        line_c = line.replace("+","").replace("E","e").rstrip().split()
        U.append(float(line_c[0]))
        a = float(line_c[1]) * 1000
        fre.append(a)
    meritve_2.append([fre, U])


fig1 = plt.figure()
ax1 = fig1.gca()
ax1.set(title = "I-U karakteristika pri različnih temepraturah", xlabel ="U[V]", ylabel = "I_C/I")

import math as m
a = 0.4
aa = m.tan(a)
print(a)

n = 10000
a = [m.atan(i*0.01) for i in range(n)]
b = [i for i in range(n)]
fig = plt.figure()
ax2 = fig.gca()
ax2.plot(a, b)
plt.show()"""