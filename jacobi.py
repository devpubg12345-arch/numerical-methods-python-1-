import numpy as np

A = np.array([[4,1,1],
              [2,7,1],
              [1,-3,12]])

b = np.array([7, -8, 6])

x = np.zeros(3)

for _ in range(10):
    x_new = np.zeros_like(x)
    for i in range(len(A)):
        s = sum(A[i][j]*x[j] for j in range(len(A)) if j != i)
        x_new[i] = (b[i] - s)/A[i][i]
    x = x_new

print("Solution:", x)