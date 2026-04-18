import numpy as np

def f(x):
    return x**2

a, b, n = 0, 1, 10
h = (b-a)/n

x = np.linspace(a,b,n+1)
y = f(x)

I = h/3*(y[0] + y[-1] + 4*sum(y[1:-1:2]) + 2*sum(y[2:-2:2]))
print("Integral:", I)