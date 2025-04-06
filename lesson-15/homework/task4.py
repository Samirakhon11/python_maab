import numpy as np 
import matplotlib.pyplot as plt 

x = np.random.uniform(0, 10, 100)
y = np.random.uniform(0, 10, 100) 

plt.figure(figsize = (10, 6)) 
plt.scatter(x, y, c = np.random.rand(100), marker = 'o', alpha = 0.7) 

plt.title("Scatter")
plt.xlabel('X axis')
plt.ylabel('Y axis', rotation = 0) 
plt.grid(True) 
plt.show() 