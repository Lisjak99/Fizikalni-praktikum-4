import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from scipy import optimize

# Električna anizotropija tekočega kristala
"""temp = []
C_vz = []
C_pr = []
C_vz_0 = 52.9 * 0.001 #nF
C_pr_0 = 54.4 * 0.001 #nF

mer = open("meritve.txt", "r")

for line in mer:
    line_c = line.replace("&","").rstrip().split(" ")
    temp.append(float(line_c[0]))
    C_vz.append(float(line_c[1]))
    C_pr.append(float(line_c[2]))

eps_vz = np.array(C_vz) / C_vz_0
eps_pr = np.array(C_pr) / C_pr_0

eps_delta = eps_vz - eps_pr
eps_povp = (2 * eps_pr + eps_vz) / 3

# Graf
podatki = [eps_vz, eps_pr, eps_povp]
ime = [r'$\epsilon_{\parallel} $', r'$\epsilon_{\perp} $', r'$\overline{\epsilon} $']
barve = ["red", "violet", "gray"]

fig1 = plt.figure()
ax1 = fig1.gca()
ax1.set(title = "Dielektrična anizotropija tekočega kristala", xlabel = "T[K]", ylabel = r'$\epsilon $')
for i in range(3):
    ax1.plot(temp[:], podatki[i][:], c = barve[i], marker = ".", label = ime[i] )
    handles, labels = ax1.get_legend_handles_labels()
    ax1.legend(handles, labels, fontsize = 10)

x = [58.0, 58.0]
y = [0.0, 17.5]
ax1.plot(x, y, label= "T= 58 r'$\epsilon $'")
plt.grid()

fig2 = plt.figure()
ax2 = fig2.gca()
ax2.set(title = "Dielektrična anizotropija ", xlabel = "T[C]", ylabel = r'$\epsilon $')
ax2.plot(temp[:], eps_delta[:], marker = ".", label = r'$\Delta \epsilon $' )

ax2.plot(x, y, label= "T= 58 r'$\epsilon $'")
plt.grid()
"""

# Frederiksov prehod
omega = 10 #kilo herz
tok = []
napetost = []
mer_f = open("meritve_fr.txt", "r")

for line in mer_f:
    line_c = line.rstrip().split(" ")
    napetost.append(float(line_c[0]))
    tok.append(float(line_c[1]))

C = np.array(tok) / (omega * np.array(napetost) ) 
U_rms = napetost / np.sqrt(2)

# Graf 
fig3 = plt.figure()
ax3 = fig3.gca()
ax3.set(title = "Frederiksov prehod", xlabel = r'$U_{RMS}$' , ylabel =  "C[mikroF]")
ax3.plot(U_rms[:], C[:], marker = ".", label = "meritve")

m1, b1 = np.polyfit(U_rms[4:9], C[4:9], 1)
ax3.plot(U_rms[4:9], m1 * U_rms[4:9] + b1, alpha = 0.5, label="Prilagoditvena krivulja")

x = [1.35, 1.35]
y = [0.0, 0.1]
ax3.plot(x, y, label= "kritična napetost")

handles, labels = ax3.get_legend_handles_labels()
ax3.legend(handles, labels, fontsize = 10)
plt.grid()
plt.show()

K_1 = (1.35/3.14)**2 * 2.0 *  8.854 * 10**(-12)
print(K_1)