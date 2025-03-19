import numpy as np

array = np.random.randint(0, 100, (10, 10))
maximum = np.max(array, axis = 0)
minimum = np.min(array, axis = 0)
#print(array)
print(max(maximum))
print(min(minimum)) 