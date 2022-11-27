from tkinter import Label
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from scipy import optimize
from scipy.optimize import curve_fit


#plt.rcParams['text.usetex'] = True

# 1.del 
meritve = ["1_15.txt", "1_35.txt", "1_55.txt"]
mer = []
for el in meritve:
    U = []
    I = []
    podatki = open(el, "r")
    for line in podatki:
        line_c = line.replace("+","").replace("E","e").rstrip().split()
        U.append(float(line_c[0]))
        I.append(float(line_c[1]))
    mer.append([U, I])

I_1 = [mer[0][1][0],mer[1][1][0] ,mer[2][1][0]]

# Grafi
fig1 = plt.figure()
ax1 = fig1.gca()
ax1.set(title = "I-U karakteristika pri različnih temepraturah", xlabel ="U[V]", ylabel = "I_C/I")
"""ax1.set_xlabel(r'U_{BC}[V]')
ax1.set_ylabel(r'log(\frac{I_{c}}{I_{o}}')
"""
barve = ["violet", "green", "blue"]
barve_2 = ["purple", "yellow", "lightblue"]
imena = ["15.9°C", "37.2°C", "54.4°C"]

koef = []
zac_vred = []
koef_nap = []

for i, el in enumerate(mer):
    I = I_1[i]
    log_I = [np.log(j/I) for j in el[1][:]]
    U_B = np.array(el[0][:])
    ax1.scatter(U_B, log_I[:], c= "{}".format(barve[i]), label = imena[i])
    
    # fit
    handles, labels = ax1.get_legend_handles_labels()
    res = stats.linregress(U_B, log_I[:])
    a = res.slope
    ax1.plot(U_B,  res.intercept + res.slope*U_B, c = "{}".format(barve_2[i]), label = f"Naklon premice: {res.slope:.2f}" )
    handles, labels = ax1.get_legend_handles_labels()
    ax1.legend(handles, labels, fontsize = 8)

    koef.append(float(a))
    zac_vred.append(float(res.intercept))
    koef_nap.append(float(res.stderr))

print()

# Izračun Boltzmanove konstante:
T_1 = np.array([float(i.replace("°C","")) for i in imena]) + 273
T_nap = 1/100
koef = np.array(koef)
koef_nap = np.array(koef_nap)
e_0 = 1.602 * 10**(-19)

k_b = []
kb_n = []

for i in range(len(T_1)):
    k_b.append(e_0/(koef[i]*T_1[i]))
    kb_n.append((T_nap + koef_nap[i])*e_0/(koef[i]*T_1[i]))

k_b_KONCEN = np.sum(np.array(k_b))/3
POV_NAP = np.sum(koef_nap)/3

print(k_b_KONCEN* POV_NAP)
# 2. del
u_2 = 0.74 
T = []
I_2 = []
aaa = open("2_.txt", "r")
for line in aaa:
    line_c = line.replace("+","").replace("E","e").rstrip().split()
    T.append(float(line_c[0]))
    I_2.append(float(line_c[1]))

I_TEST = I_2[0]
log_I2 = [np.log(j/I_TEST) for j in I_2[:]]

fig2 = plt.figure()
ax2 = fig2.gca()
ax2.set(title = "I-T karakteristika pri napetosti U = 0.74V", xlabel ="T[°C]", ylabel = "I_C/I")

ax2.scatter(T[:], log_I2[:], label = "Odvisnost logaritma I_C/I")
res2 = stats.linregress(T[:], log_I2[:])
ax2.plot(T[:], res2.intercept + res2.slope*np.array(T[:]))
#temp, kjer doseže razmerje log 0

handles, labels = ax2.get_legend_handles_labels()
ax2.legend(handles, labels, fontsize = 8)


fig3 = plt.figure()
ax3 = fig3.gca()
ax3.set(title = "I-T karakteristika pri napetosti U = 0.74V", xlabel ="T[°C]", ylabel = "I_C")

ax3.scatter(T[:], I_2[:], label = "Odvisnost toka I_C")
handles, labels = ax3.get_legend_handles_labels()
ax3.legend(handles, labels, fontsize = 8)


# Izračun Saturacijskega toka
u_b = 0.74
J_S =  I_2[0] * np.exp(-(e_0/(k_b_KONCEN*(289)) * u_b))
print(J_S)
    

