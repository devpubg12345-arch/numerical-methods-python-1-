import numpy as np

A = np.array([[2,1],
              [1,2]])

x = np.array([1,1])

for _ in range(10):
    x = A @ x
    x = x / max(abs(x))

print("Eigenvector:", x)