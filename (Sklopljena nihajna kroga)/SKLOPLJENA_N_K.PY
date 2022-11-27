from tkinter import Label
import numpy as np
import math as m
import matplotlib.pyplot as plt
from scipy import stats
from scipy import optimize
from scipy.optimize import curve_fit
import xml.etree.ElementTree as ET
import csv 

# 1.DEL - 

vhod = []
ch1 = []
ch2 = []
ch3 = []
ch4 = []

meritve_1 = ["1_0000.csv", "1_0150.csv", "1_0330_M.csv", "1_0560.csv", "1_0820.csv", "1_1150_C.csv"]
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
            vhod_v.append(float(line[0]))
            ch1_v.append(float(line[1]))
            ch2_v.append(float(line[2]))
            ch3_v.append(float(line[3]))
            ch4_v.append(float(line[4]))
    vhod.append(vhod_v)
    ch1.append(ch1_v)
    ch2.append(ch2_v)
    ch3.append(ch3_v)
    ch4.append(ch4_v)
    vhod_v = []
    ch1_v = []
    ch2_v = []
    ch3_v = []
    ch4_v = []

# Grafi
fig1 = plt.figure()
ax1 = fig1.gca()
ax1.set(title = "Odziv 1. in 2. nihajnega kroga na napetostno stopnico, C = 0pF")

fig2 = plt.figure()
ax2 = fig2.gca()
ax2.set(title = "Odziv 1. in 2. nihajnega kroga na napetostno stopnico, C = 150pF")

fig3 = plt.figure()
ax3 = fig3.gca()
ax3.set(title = "Odziv 1. in 2. nihajnega kroga na napetostno stopnico, C = 330pF")

fig4 = plt.figure()
ax4 = fig4.gca()
ax4.set(title = "Odziv 1. in 2. nihajnega kroga na napetostno stopnico, C = 560pF")

fig5 = plt.figure()
ax5 = fig5.gca()
ax5.set(title = "Odziv 1. in 2. nihajnega kroga na napetostno stopnico, C = 820pF")

fig6 = plt.figure()
ax6 = fig6.gca()
ax6.set(title = "Odziv 1. in 2. nihajnega kroga na napetostno stopnico, C = 1150pF")

ax = [ax1, ax2, ax3, ax4, ax5,ax6]
ime = [0, 150, 330, 560, 820,1150]
max_A = np.array([0.0085, 0.0085, 0.0082, 0.0081, 0.0080, 0.0076]) * 0.368
x = [0, 0.0005]
for i, el in enumerate(ax):
    y = [max_A[i],max_A[i]]

    el.plot(np.array(vhod[i]), np.array(ch1[i]), marker=".")
    el.plot(np.array(vhod[i]), np.array(ch2[i]), marker=".", color="red")    
    el.plot(x,y)


# Odčitane vrednosti iz grafov:



# 2. del - 
mer_2 = ["2_1.dat", "2_3.txt"]
meritve_2 = []
for el in mer_2:
    U = []
    fre = []
    mer = open(el, "r")
    for line in mer:
        line_c = line.replace("+","").replace("E","e").rstrip().split()
        U.append(float(line_c[0]))
        fre.append(float(line_c[1]))
    meritve_2.append([fre, U])


fig1 = plt.figure()
ax1 = fig1.gca()
ax1.set(title ="Resonančna krivulja", xlabel =r"$\nu  [Hz]$", ylabel = "U[V]")

ime = ["Kratko sklenjen 2. krog", "Brez kratkega stika"]
for i, el in enumerate(meritve_2):
    ax1.plot(np.array(el[1]), np.array(el[0]), label="{}".format(ime[i]))

# delta omega 
w_max = 0.1169
x = [65000, 75000]
y = [w_max * np.sqrt(1/2), w_max * np.sqrt(1/2)]
ax1.plot(x, y,"r--", label= r"$\Delta \omega = 2100 Hz$")

x1 = [66800, 66800]
y1 = [0, 0.12]
ax1.plot(x1, y1,"g--", label =r"$\omega_{1} = 66800 Hz$")

x2 = [68940, 68900]
y2 = [0, 0.12]
ax1.plot( x2, y2,"g--", label =r"$\omega_{1} = 68940 Hz$")

handles, labels = ax1.get_legend_handles_labels()
ax1.legend(handles, labels, fontsize = 8)

A = 68000/2100
nap_A = (200/68000) + (200/2100)


# 3.del - Sklopljena nihajna kroga
# vse meritve na 2. tuljavi
mer_3 = ["3_150pf.dat","3_330pf.dat","3_560pf.dat","3_820pf.dat","3_1150pf.dat"]
imena_1 = ['0.txt', "150.txt", "330.txt", "560.txt", "820.txt", "1150.txt"]

meritve_3 = []
for el in mer_3:
    U = []
    fre = []
    mer = open(el, "r")
    for line in mer:
        line_c = line.replace("+","").replace("E","e").rstrip().split()
        U.append(float(line_c[0]))
        fre.append(float(line_c[1]))
    meritve_3.append([fre, U])

fig2 = plt.figure()
ax2 = fig2.gca()
ax2.set(title ="Resonančna krivulja - sklopitev", xlabel =r"$\nu  [Hz]$", ylabel = "U[V]")

ime_3 = [150, 330, 560, 820, 1150]
for i, el in enumerate(meritve_3):
    ax2.plot(np.array(el[1]), np.array(el[0]), label="C = {}pf".format(ime_3[i]))

handles, labels = ax2.get_legend_handles_labels()
ax2.legend(handles, labels, fontsize = 8)

# primerjava napetosti u1 in u2 pri max sklopitvi
mer_3_b = ["1150pf-u1.dat", "1150pf-u2.dat" ]

meritve_3b = []
for el in mer_3_b:
    U = []
    fre = []
    faza = []
    mer = open(el, "r")
    for line in mer:
        line_c = line.replace("+","").replace("E","e").rstrip().split()
        U.append(float(line_c[0]))
        fre.append(float(line_c[1]))
        a = float(line_c[1])* 100000
        faza.append(m.atan(a))

    meritve_3b.append([fre, U, faza])

fig3 = plt.figure()
ax3 = fig3.gca()
ax3.set(title ="Meritev napetosti pri sklopitvi 1150pf na obeh krogih", xlabel =r"$\nu  [Hz]$", ylabel = "U[V]")

ime_3 = [1, 2]
for i, el in enumerate(meritve_3b):
    ax3.plot(np.array(el[1]), np.array(el[0]), label="Nihajni krog {}".format(ime_3[i]))

handles, labels = ax3.get_legend_handles_labels()
ax3.legend(handles, labels, fontsize = 8)

# graf faze
fig4 = plt.figure()
ax4 = fig4.gca()
ax4.set(title ="Primerjava faze", xlabel =r"$\nu  [Hz]$", ylabel = "U[V]")

ime_3 = [1, 2]
for i, el in enumerate(meritve_3b):
    ax4.plot(np.array(el[1]), np.array(el[2]), label="Nihajni krog {}".format(ime_3[i]))

handles, labels = ax4.get_legend_handles_labels()
ax4.legend(handles, labels, fontsize = 8)

plt.show()
ime_n = ["0", "150", "330", "560", "820", "1150"]
beta = 1 / np.array([0.000125, 0.00016, 0.00018, 0.000185, 0.000178, 0.00018])
delta_beta = beta * 0.02
DEL_OMEGA = (2 * np.pi ) / np.array([0.0005, 0.000304, 0.000165, 0.000116, 9.5 * 10**(-5), 7.6 * 10**(-5)])
delta_omega = DEL_OMEGA * 0.02
with open("latex.txt", "w") as f:
    for i in range(6):
        f.write(ime_n[i] + " &" + str(round(beta[i])) + " &" + str(round(delta_beta[i])) + " &" + str(round(DEL_OMEGA[i])) + " &" + str(round(delta_omega[i])) + "\\" + "\\" + "\n")

# "{}".format(beta[i]) + " &" + "{}".format(delta_beta[i]) + " &" + "{}".format(DEL_OMEGA[i]) + " &" + "{}".format(delta_omega[i]) + "\\" + "\\" + "\n"