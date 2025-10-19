# Set up
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sps
import control as ct
from control.matlab import *

a = 4
b = 5
c = 3


# sample root loci plots

Np = 5.5 * c * np.array([ 1, 7.3*a + 2*b])
Dp = np.polymul(np.array([1, 2.3*a]), np.array([1, 8.7*a + 3.1*b + 2*c]))
Gp = ct.tf(Np,Dp)      # Plant

# Ideal PID controller
# will add practical part later

z1 = 12
z2 = 18
k = 1

Nc = np.polymul( np.array([1, z1]), np.array([1, z2]))
Dc = np.array([1, 0])
Gc = ct.tf(Nc, Dc)     #Controller 

Go = series(Gp,Gc)  # open loop 


plt.figure(figsize=(12,5))
plt.axvline(x=-11.3,color='b',linestyle='--', label="-11.3")
R, K = ct.root_locus_plot(Go, plot=True, color='r',label="_")
plt.xlabel("Real")
plt.ylabel("Imaginary")
plt.xlim((-60,1))
plt.grid(True)
plt.show()