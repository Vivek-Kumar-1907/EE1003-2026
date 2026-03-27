from matplotlib import legend
import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

x = np.linspace(0, 1000, num=100000)
y0 = np.ones(100000)

y1 = integrate.cumulative_simpson(y0, x=x, initial = 0)
y2 = integrate.cumulative_simpson(y1, x=x, initial = 0)
y3 = integrate.cumulative_simpson(y2, x=x, initial = 0)

plt.plot(x, y1, label = "x1=t")
plt.plot(x, y2, label = "x2=t^2/2")
plt.plot(x, y3, label = "x3=t^3/6")
plt.legend()

plt.xlabel("t-axis")
plt.xlim(0,4)
plt.ylabel("x-axis")
plt.ylim(0,10)
plt.title("Plot for integrals of x=t")
