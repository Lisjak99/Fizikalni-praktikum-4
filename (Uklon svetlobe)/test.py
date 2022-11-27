import numpy as np 
import matplotlib.pyplot as plt
from scipy import stats
from scipy import optimize
import pandas as pd

fig1 = plt.figure()
ax1 = fig1.gca()
ax1.set(title = "Intenziteta v odvisnosti od odmika", xlabel = "odmik", ylabel = "Intenzite")

mer1 = np.loadtxt("5_1.dat", unpack = True)
odmik1 = mer1[0]
amplituda1 = mer1[1]

ax1.scatter(odmik1, amplituda1)

plt.show()