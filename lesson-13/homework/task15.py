import numpy as np

matrix = np.random.randint(0, 10, (5, 5))

row_sums = np.sum(matrix, axis=1)
col_sums = np.sum(matrix, axis=0)

print("Matrix (5x5):\n", matrix)
print("\nRow-wise Sums:\n", row_sums)
print("\nColumn-wise Sums:\n", col_sums)
