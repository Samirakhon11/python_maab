import numpy as np

matrix1 = np.random.randint(0, 20, (3, 3))
matrix2 = np.random.randint(0, 20, (3, 3)) 

mult = np.dot(matrix1, matrix2)

print(mult) 