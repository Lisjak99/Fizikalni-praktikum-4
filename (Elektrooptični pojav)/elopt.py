import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from scipy import optimize
from scipy.optimize import curve_fit

# Kotna odvisnost prepustnosti polarizatorja
koti_1 = [5 * i for i in range(37)]
koti =  2 * np.pi * (1/360) * np.array(koti_1[::-1])

tok = {}

meritve = ["1-1.txt","1-2.txt","2-1.txt","2-2.txt","3-1.txt","3-2.txt"]
I_0 = [1.44334e-4 * 0.6, 3.17123e-4 * 0.6,1.13740e-6 * 0.09]
for i in range(len(meritve)):
    a = meritve[i]
    mer = open(a)
    vmesni_t = []
    for line in mer:
        line_c = line.replace("E", "e").rstrip().split()
        vmesni_t.append(float(line_c[1]))
    tok[i] = np.array(vmesni_t)
    vmesni_t.clear()

"""#meritve za pdf
a = open("poskus.txt", "w")
for i in range(37):
    a.write(str(koti[i]))
    a.write("&") 
    a.write(str(prvi[i]))
    a.write("\\")
    a.write("\\")
    a.write("\n")
"""

"""
# Graf 1. del
prvi = tok[1] / (3.17123e-4 * 2.3)

fig1 = plt.figure()
ax1 = fig1.gca()
ax1.set(title = "Prepustnost v odvisnosti od kota", xlabel = "Kot[rad]", ylabel = "I/I0")
ax1.scatter(koti[:], prvi[:],label="Meritev") 

def fit_prvi(x,P_1,delta, P_0):
    return P_1 * (np.sin(x + delta))**2 + P_0
init_val_prvi = [1,1,1]
fitpar, fitcov = curve_fit(fit_prvi, xdata=koti, ydata=prvi, p0=init_val_prvi, absolute_sigma=True )
yfit = fit_prvi(koti, fitpar[0], fitpar[1], fitpar[2])
ax1.plot(koti, yfit, label=r"$P_{p} = P_{1}* sin^{2}(\beta + \delta) + P_{0}$")

handles, labels = ax1.get_legend_handles_labels()
ax1.legend(handles, labels, fontsize = 10)

"""
"""
# Graf 2.del
drugi = tok[2] / (1.13740e-6)

fig2 = plt.figure()
ax2 = fig2.gca()
ax2.set(title = "Prepustnost v odvisnosti od kota", xlabel = "Kot[]", ylabel = "I/I_0")
ax2.scatter(koti[:], drugi[:],label="Meritev") 

def fit_drugi(x,P_1,delta, P_0):
    return P_1 * (np.sin(x + delta))**2 + P_0
init_val_drugi = [1,1,1]
fitpar2, fitcov = curve_fit(fit_drugi, xdata=koti, ydata=drugi, p0=init_val_drugi, absolute_sigma=True )
yfit2 = fit_drugi(koti, fitpar2[0], fitpar2[1], fitpar2[2])
ax2.plot(koti, yfit2, label=r"$P_{p} = P_{1}sin^{2}(2\beta + \delta) + P_{0}$")
#"P_0 = {}, P_1 = {}, \delta = {}".format()
handles, labels = ax2.get_legend_handles_labels()
ax2.legend(handles, labels, fontsize = 10)

"""
# 3. del - kerrova celica
U_3 = []
I_3 = []
y_error = [0.0005*i for i in range(29)]

mer = open("prirejena_meritev_3.txt", "r")
for line in mer:
    line_c = line.rstrip().split()
    print(line_c)
    U_3.append(float(line_c[0]))
    I_3.append(float(line_c[1]))

d = 1.4 * 10**(-3)
L = 1.5 * 10**(-3)
alfa = np.pi * L * (1/d**2)

x = np.linspace(0, 1000, 100)

fig3 = plt.figure()
ax3 = fig3.gca()
ax3.set(title = "Prepustnost od napetosti na Kerrovi celici", xlabel = "U[V]", ylabel = "I[A]")
ax3.scatter(U_3[:], I_3[:], label="Meritve")
plt.errorbar(U_3[:], I_3[:], yerr = y_error,fmt='.',
             ecolor = 'pink',color='blue', label ="Napaka meritev")

def fit_drugi(x,P_1,B, fi):
    return P_1 * (np.sin(alfa*B*x**2 + fi/2))**2 

init_val_tretji = [1,10**-9,1]
fitpar3, fitcov = curve_fit(fit_drugi, xdata=U_3, ydata=I_3, p0=init_val_tretji, absolute_sigma=True )
yfit3 = fit_drugi(x, fitpar3[0], fitpar3[1], fitpar3[2])


ax3.plot(x, yfit3, label="Prilagoditvena krivulja")

handles, labels = ax3.get_legend_handles_labels()
ax3.legend(handles, labels, fontsize = 10)

plt.tight_layout()
plt.show()