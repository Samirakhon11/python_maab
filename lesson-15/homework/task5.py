import numpy as np 
import matplotlib.pyplot as plt 

data = np.random.normal(loc = 0, scale = 1, size = 100)

plt.figure(figsize = (10, 6))
plt.hist(data, bins = 30, alpha = 0.7, color = 'blue', edgecolor = 'black') 

plt.title('Histogram')
plt.xlabel('Value')
plt.ylabel('Frequency')

plt.grid(axis='y', alpha=0.75)
plt.show()