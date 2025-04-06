import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 1000)
y1 = x ** 3
y2 = np.sin(x)
y3 = np.exp(x)
y4 = np.log(x + 1) 

fig, axs = plt.subplots(2, 2, figsize = (10, 6))

axs[0,0].plot(x, y1, label = '$x^3$', color = 'r') 
axs[0, 0].set_title('Plot 1')
axs[0, 0].legend()

axs[0,1].plot(x, y2, label = '$\sin(x)$', color = 'b') 
axs[0, 1].set_title('Plot 2')
axs[0, 1].legend()

axs[1,0].plot(x, y3, label = '$e^x$', color = 'g') 
axs[1, 0].set_title('Plot 3')
axs[1, 0].legend()

axs[1,1].plot(x, y4, label = '$\log(x + 1)$', color = 'y')   
axs[1, 1].set_title('Plot 4')
axs[1, 1].legend() 

plt.tight_layout()
plt.show() 