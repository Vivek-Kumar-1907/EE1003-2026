import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
import math

def integrand(t, s, a):
  return (t**a)*np.pow(np.e, -s*t)/math.factorial(a)
  
n = 100
S = np.linspace(0, 10, num = n)
lt_1 = np.zeros(n)
lt_2 = np.zeros(n)
lt_3 = np.zeros(n)
for i in range(0, n):
  lt_1[i],_ = integrate.quad(integrand, 0, np.inf, args=(S[i], 1))
  lt_2[i],_ = integrate.quad(integrand, 0, np.inf, args=(S[i], 2))
  lt_3[i],_ = integrate.quad(integrand, 0, np.inf, args=(S[i], 3))
plt.plot(S, lt_1, label = 's-transform of f(t) = t -> F(s) = 1/s^2')
plt.plot(S, lt_2, label = 's-transform of f(t) = t^2/2 -> F(s) = 1/s^3')
plt.plot(S, lt_3, label = 's-transform of f(t) = t^3/3 -> F(s) = 1/s^4')
plt.xlim(0, 4)
plt.ylim(0, 4)
plt.legend()
plt.xlabel('s-axis')
plt.ylabel('F(s)')
plt.title('Plot after computing laplace transform')
