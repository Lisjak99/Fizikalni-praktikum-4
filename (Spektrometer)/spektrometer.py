from tkinter import Label
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from scipy import optimize
from scipy.optimize import curve_fit

# 1.del - umeritev
lambde_u = np.array([577, 579, 546, 436, 656, 486, 434])#
kot_u =  np.abs(np.array([55.5, 55.5, 56.0, 60.2, 55.3, 58.8, 59.5]) - 360)

#kot_u =  np.array([311.25, 313, 310.58, 319.17, 313, 309.5]) 


fig1 = plt.figure()
ax1 = fig1.gca()
ax1.set(title= "Umeritvena krivulja", xlabel =r"$\lambda [nm]$", ylabel = "kot[°]")

ax1.scatter(lambde_u, kot_u, label = "Meritve")

def fit_umeritve(x,a,b,c):
    return a + b * x + c * np.sqrt(x)

init_vals = [170,-0.2,10]
fitpar, fitcov = curve_fit(fit_umeritve, xdata=lambde_u, ydata=kot_u, p0=init_vals, absolute_sigma=True)
y_fit_umeritve = fit_umeritve(lambde_u, fitpar[0], fitpar[1], fitpar[2])
ax1.plot(lambde_u, y_fit_umeritve, label=r"$Krivulja: kot = a + b\lambda + c\sqrt{\lambda} $")

handles, labels = ax1.get_legend_handles_labels()
ax1.legend(handles, labels, fontsize = 10)


# 2. del - izmerjeni spektri
napaka = 1 - 0.97
spektri = {
    "varcna": (np.array([59.0, 58.5, 56.4, 56.2, 55.5]), ["lightblue", "green", "yellow", "orange", "red"]),
    "volframska":  (np.array([58.5, 57.0, 56.7, 55.9]), ["lightblue", "green", "orange", "red"]),
    "NO_2":  (np.array([58.5, 58.7, 57.7, 57.3, 56.6, 56.5, 55.4, 55.1]), ["lightblue", "blue", "green", "lime","greenyellow", "yellow", "orange", "tomato", "red" ]),
    "He": (np.array([59.2, 58.6, 58.4, 56.2, 55.5, 54.4]), ["darkblue", "navy", "lightblue",  "orange", "red", "red"]),
    "Ne": (np.array([57.4, 57.1, 56.2, 55.9, 55.8]), ["lightblue", "green", "greenyellow", "orange", "red"])
}
imena = [i for i in spektri.keys()]
vsi = []
for j, ime in enumerate(imena):

    rezultati = []
    def izracun(sez, a = 10.4, b = -0.2, c = 170.7):
        vrednosti = []
        sez = np.abs(sez - 360)

        for i in sez:
            if a**2 - 4*b*(c-i) < 0:
                vrednosti.append(None)
                i +=1
            r_plus = ( (-a + np.sqrt( a**2 - 4*b*(c-i))) / (2*b))**2
        #r_minus = ( (-a - np.sqrt( a**2 - 4*b*(c-i))) / (2*b))**2

            vrednosti.append(r_plus)

        zao_vrednosti = [(round(el, 2)) for el in vrednosti]

        with open(ime + ".txt", "w") as f:
            for i,el in enumerate(sez):
                f.write("{}".format(el) + "& " + "{}".format(zao_vrednosti[i])+ "& " + "{}".format(round(zao_vrednosti[i] * napaka),2)+ "& " +"{}".format(spektri[ime][1][i]) + "\\" + "\\" + "\n")

        rezultati.append(vrednosti)
        return vrednosti

    izracun(spektri[ime][0])
    vsi.append(rezultati)
    print(rezultati)

# spreminjaj parameter 

