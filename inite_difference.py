def f(x):
    return x**2

x = 2
h = 0.01

forward = (f(x+h)-f(x))/h
backward = (f(x)-f(x-h))/h
central = (f(x+h)-f(x-h))/(2*h)

print(forward, backward, central)