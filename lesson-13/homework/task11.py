import numpy as np

matrix = np.random.randint(0, 10, (3, 3))
determinant = np.linalg.det(matrix) 

print(round(determinant, 2)) 