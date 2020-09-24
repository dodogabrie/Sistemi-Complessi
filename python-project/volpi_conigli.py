from scipy.integrate import odeint
import matplotlib.pyplot as plt
import numpy as np
def func(y,t, c, k1, k2, k3):
    r,s = y 
    drds = [k1*c*r-k2*r*s, k2*r*s - k3*s]
    return drds
k1 = 1
k2 = 5
k3 = 1
c = 3
t0 = [10, 10]
t = np.linspace(0,10,1000)
sol = odeint(func, t0, t, args=(k1, k2, k3, c))
plt.plot(t, sol[:, 0], 'b', label='conigli')
plt.plot(t, sol[:, 1], 'g', label='volpi')
plt.legend(loc='best')
plt.xlabel('t')
plt.grid()
plt.show()
