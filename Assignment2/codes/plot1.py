import numpy as np
import matplotlib.pyplot as plt
import math

def g_x(a, x):
  return math.sqrt(a)*(1+((3*a**2)/x**2)) - 3*(a**2)/x

n=1001
print('Enter a:')
a=float(input())
x = np.arange(1, n+1)
y = np.zeros(n)
y[0] = 1
for i in range(1,n):
  y[i] = g_x(a, y[i-1])
plt.plot(x, y, label = 'x_n')
#plt.xlim(0, 25)
plt.xlabel('n')
plt.ylabel('x_n')
plt.legend()
plt.title(f'x_n vs n for a = {a}')
print(f'x_n after {n-1} iterations: x_{n-1} = {y[n-1]}')
