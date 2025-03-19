import numpy as np

matrix = np.random.randint(0, 10, (3, 3))
vector = np.random.randint(0, 10, (3, 1))

result = np.dot(matrix, vector)  

print("Matrix (3x3):\n", matrix)
print("\nColumn Vector (3x1):\n", vector)
print("\nMatrix-Vector Product (3x1):\n", result)
