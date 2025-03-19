import numpy as np

vector = np.random.randint(0, 50, (30,))
mean = np.sum(vector) / 30
print(vector) 
print(round(mean, 2))  