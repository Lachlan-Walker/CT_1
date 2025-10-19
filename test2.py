import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sps
import control as ct
from control.matlab import *

a = 4
b = 5
c = 3

mu = 1 + (a + 10) / 30
w_n = (c + 10) / 15

Np = np.array([1])
Dp = np.array([1, -mu * w_n, w_n**2])

Gp = tf(Np,Dp)

z1 = 1.5
z2 = 2
k = 1


Nc = np.polymul( np.array([1, z1]), np.array([1, z2]))
Dc = np.array([1, 0])
Gc = ct.tf(Nc, Dc)     #Controller 

Go = series(Gp,Gc)  # open loop 


plt.figure(figsize=(12,5))
plt.axvline(x=-0.66,color='b',linestyle='--', label="-11.3")
R, K = ct.root_locus_plot(Go, plot=True, color='r',label="_")
plt.xlabel("Real")
plt.ylabel("Imaginary")
plt.xlim((-25,1))
plt.grid(True)
plt.show()