def f(x, y):
    return x + y

x, y = 0, 1
h = 0.1

for _ in range(10):
    k1 = h*f(x,y)
    k2 = h*f(x+h/2, y+k1/2)
    k3 = h*f(x+h/2, y+k2/2)
    k4 = h*f(x+h, y+k3)
    
    y += (k1+2*k2+2*k3+k4)/6
    x += h

print("y:", y)