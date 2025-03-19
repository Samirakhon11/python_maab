import numpy as np

A = np.random.randint(0, 10, (3, 3))
B = np.random.randint(0, 10, (3, 1))

x = np.linalg.solve(A, B)

print("Matrix A:\n", A)
print("\nColumn Vector b:\n", B)
print("\nSolution Vector x:\n", x)
