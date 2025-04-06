import numpy as np
import matplotlib.pyplot as plt

figure = plt.figure()
axis = plt.axes(projection = '3d')

x = np.linspace(-5, 5, 1000)
y = np.linspace(-5, 5, 1000)

xx, yy = np.meshgrid(x, y)
zz = np.cos(xx ** 2 + yy ** 2) 

surf = axis.plot_surface(xx, yy, zz, cmap = 'viridis')  

axis.set_xlabel('X axis')
axis.set_ylabel('Y axis')
axis.set_zlabel('Z axis')

figure.colorbar(surf, ax=axis, shrink = 0.5, aspect = 10) 

plt.title('3D Surface Plot') 
plt.show() 