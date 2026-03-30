import numpy as np
import matplotlib.pyplot as plt
import math

def g_x(a, x):
  return math.sqrt(a)*(1+((3*a**2)/x**2)) - 3*(a**2)/x

n=120
print('Enter a:')
a=float(input())
x = np.arange(1, n+1)
y = np.zeros(n)
y[0] = 1
for i in range(1,n):
  y[i] = g_x(a, y[i-1])
z = np.zeros(n)
for i in range(1, n):
  z[i] = np.log(np.abs(y[i] - y[n-1]))
plt.plot(x, z, label = 'x_n')
plt.xlabel('n')
plt.ylabel(f'log(x_n-{math.sqrt(a)})')
plt.legend()
plt.title(f'log_10(x_n-{math.sqrt(a)}) vs n for a = {a}')
print(f'log_10(x_n-{math.sqrt(a)}) after {n-1} iterations: {z[n-1]}')
