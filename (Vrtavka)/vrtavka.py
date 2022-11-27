from re import L
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from scipy import optimize
from scipy.optimize import curve_fit

# Meritve
a = [25.5, 24, 15.7, 19, 18.5, 18, 18, 16.5, 16, 16]
t_0 = np.array(a) / 10
w = 2 * np.pi / t_0


c = 6/30
ww =  2 * np.pi / c


# Izračuni nutacije in precesije
Odd = [0.426,0.426,0.426, 0.426 + 0.45, 0.426 + 0.45, 0.426 + 0.45, 0.426 + 0.75, 0.426 + 0.75, 0.426 + 0.75]
L = [0, 0, 0, 0.45, 0.45, 0.45, 0.75, 0.75, 0.75]
W_z = [600, 500, 400,600, 500, 400, 600, 500, 400]
J_33 = 1389.65
J_11 = 3280.3 
delta_l = 0.1/4.5

w_n_izracun = []
w_pr_izracun = []

for i in range(9):
    w_n_izracun.append(W_z[i] * J_33/ (J_11 + Odd[i]**2 * 18))

delta_w_n_izracun = np.array(w_n_izracun) * delta_l
delta_w_pr_izracun = np.array(w_pr_izracun) * delta_l

m = 515 + 15 + 27 + 18
g = 9.81
l = 0.426 

for i in range(9):
    w_pr_izracun.append((m * g * (l + L[i]))/(J_33 * W_z[i]))
    print()

w_n_i_zaokrozene = np.round(w_n_izracun, decimals= 1)
w_pr_i_zaokrozene = np.round(w_pr_izracun, decimals= 1)

w_pr_izracun_nova = np.array(w_pr_izracun) * 1000
delta_w_pr_izracun = np.array(w_pr_izracun_nova) * delta_l

print(w_n_i_zaokrozene)
print("---------------------------------------------")
print(delta_w_n_izracun)
print("=============================================")
print(w_pr_izracun_nova)
print("-----------------------------------------")
print(delta_w_pr_izracun)

