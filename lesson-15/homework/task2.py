import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, (2 / np.pi), 10000) 
y1 = np.sin(x)
y2 = np.cos(x) 

plt.plot(x, y1, label = '$\sin(x)$', linestyle = ':', marker = 'o', markevery = 500)
plt.plot(x, y2, label = '$\cos(x)$', linestyle = '-', marker = 's', markevery = 500)  
plt.xlabel('X')
plt.ylabel('Y', rotation = 0)
plt.legend() 
plt.show()