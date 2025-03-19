import numpy as np

matrix = np.random.randint(0, 10, (4, 4))
trans = matrix.T

print("Original matrix:")
print(matrix)
print("Transposed matrix:")
print(trans)