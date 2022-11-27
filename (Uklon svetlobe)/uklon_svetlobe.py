import numpy as np 
import matplotlib.pyplot as plt
from scipy import stats
from scipy import optimize
import pandas as pd
"""
# 1. del
meritve_hist = ["1_1.dat", "2_1.dat", "3_1.dat", "5_1.dat"]
#meritve_hist = ["1_1_hist.dat","2_1_hist.dat","3_1_hist.dat","5_1_hist.dat"]
mer = []
odmiki = []
amplitude = []

# 1 reža
mer1 = np.loadtxt("1.txt", unpack = True)
odmik1 = mer1[0]
amplituda1 = (np.array(mer1[1]) + 100)/80

mer2 = np.loadtxt("2.txt", unpack = True)
odmik2 = mer2[0]
amplituda2 = (np.array(mer2[1]) + 135)/80

mer3 = np.loadtxt("3.txt", unpack = True)
odmik3 = mer3[0]
amplituda3 = (np.array(mer3[1]) + 135)/80

mer5 = np.loadtxt("5_1.dat", unpack = True)
odmik5 = mer5[0]
amplituda5 = (np.array(mer5[1]) -220)/80

I_max_prve = 80
odmiki = [odmik1, odmik2, odmik3, odmik5]
amplitude = [amplituda1, amplituda2, amplituda3, amplituda5]
ime = ["1 reža", "2 reži", "3 reže", "5 rež"]
fig1 = plt.figure()
ax1 = fig1.gca()
ax1.set(title = "Intenziteta v odvisnosti od odmika", xlabel = "odmik", ylabel = "Intenzite")

for i in range(4):
    ax1.plot(odmiki[i][:], amplitude[i][:], label = ime[i], marker = ".")
    handles, labels = ax1.get_legend_handles_labels()
    ax1.legend(handles, labels, fontsize = 10)
plt.show()

# Graf navadno
I_0 = 1
fig3, (axs1, axs2, axs3, axs4) = plt.subplots(4)
fig3.suptitle("Odvisnost relativne intenzitete od odmika")

axs1.set(xlabel = "odmik", ylabel="I/I_0")
axs1.plot(odmik1,amplituda1 , marker = ".", color = "violet", label ="1 reža")
handles, labels = axs1.get_legend_handles_labels()
axs1.legend(handles, labels, fontsize = 10)

axs2.set(xlabel = "odmik [cm]", ylabel="I/I_0")
axs2.plot(odmik2, amplituda2, marker = ".", color = "purple", label ="2 reži")
handles, labels = axs2.get_legend_handles_labels()
axs2.legend(handles, labels, fontsize = 10)

axs3.set(xlabel = "odmik [cm]", ylabel="I/I_0")
axs3.plot(odmik3, amplituda3, marker = ".", color = "violet", label ="3 reže")
handles, labels = axs3.get_legend_handles_labels()
axs3.legend(handles, labels, fontsize = 10)

axs4.set(xlabel = "odmik [cm]", ylabel="I/I_0")
axs4.plot(odmik5, amplituda5, marker = ".", color = "purple", label ="5 rež")
handles, labels = axs4.get_legend_handles_labels()
axs4.legend(handles, labels, fontsize = 10)

fig2 = plt.figure()
ax2 = fig2.gca()

ax2.plot(odmik1, amplituda1)
"""

# 3.del -> 
zp = np.array([14, 15.8, 18, 20.7]) * 0.01
z0 = np.array([44, 42, 40, 37]) * 0.01
Rn = np.array([1.5, 1.2, 1.0, 0.7]) * 0.01
lambda_r = 650 * 10**(-9)

psi_in = 1/zp + 1/z0
n = Rn**2 /(lambda_r) * psi_in

fig4 = plt.figure()
ax4 = fig4.gca()
ax4.set(title = "Št. con v odvisnosti od efektivnega odmika", xlabel = "ef. odmik", ylabel = "Cone - n")

ax4.scatter(psi_in, n)

res = stats.linregress(psi_in, n)
a = round(res.slope,2)
b = round(res.intercept, 2)
c = res.stderr
print(c)
#
ax4.plot(psi_in,  res.intercept + res.slope*psi_in, c = "red", label = f"Naklon premice: {a}    n_0:{b}" )
handles, labels = ax4.get_legend_handles_labels()
ax4.legend(handles, labels, fontsize = 8)

plt.show()