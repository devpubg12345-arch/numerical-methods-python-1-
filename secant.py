def f(x):
    return x**3 - x - 2

def secant(x0, x1, tol=1e-6):
    while abs(x1 - x0) > tol:
        x2 = x1 - f(x1)*(x1-x0)/(f(x1)-f(x0))
        x0, x1 = x1, x2
    return x1

print("Root:", secant(1, 2))