import numpy as np

matrix = np.random.randint(0, 50, (5, 5))
normalized = (matrix - np.min(matrix)) / (np.max(matrix) - np.min(matrix))

print(matrix) 
print(normalized) 