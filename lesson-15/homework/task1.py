import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 1000)

def f_x(x):
    return x ** 2 - 4 * x + 4

y = f_x(x) 
plt.plot(x, y, label = '$f(x) = x^2 - 4x + 4$')  
plt.title("Parabola")
plt.xlabel('X')
plt.ylabel('Y', rotation = 0)
plt.legend() 
plt.show() 