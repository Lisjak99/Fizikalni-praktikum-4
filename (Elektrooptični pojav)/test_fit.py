import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from scipy import optimize
from scipy.optimize import curve_fit

#Hipotetičen primer
"""x = np.array([i for i in range(10)])
y = np.array([(1 + np.sin(2*j + 2)**2) for j in range(10)])
x_za_fit = np.linspace(0, 10, 100)
"""
#Moje meritve
x = np.array([5*i for i in range(37)]) * 2 * np.pi * (1/360)
toki = []
mer = open("1-2.txt")
for line in mer:
    line_c = line.replace("E", "e").rstrip().split()
    toki.append(float(line_c[1]))
y = np.array(toki)
x_za_fit = np.linspace(0, 3.2, 1000)


fig1 = plt.figure()
ax1 = fig1.gca()
ax1.scatter(x, y, label = "Meritve")

def kvadraten_fit(x, a, b, c):
    return a + b * np.sin(x +c )**2 # opomba - fit z sin(2x) ne deluje

init_vals = [1,1,1]

fitpar, fitcov = curve_fit(kvadraten_fit, xdata=x, ydata=y, p0=init_vals, absolute_sigma=True)
y_fit = kvadraten_fit(x_za_fit, fitpar[0], fitpar[1], fitpar[2])
ax1.plot(x_za_fit, y_fit)

plt.show()
