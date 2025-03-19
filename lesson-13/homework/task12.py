import numpy as np

A = np.random.randint(0, 10, (3, 4))
B = np.random.randint(0, 10, (4, 3))

result = np.dot(A, B) 

print("Matrix A (3x4):\n", A)
print("\nMatrix B (4x3):\n", B)
print("\nMatrix Product (A · B) (3x3):\n", result)