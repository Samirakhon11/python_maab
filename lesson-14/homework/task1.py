import numpy as np

array = np.array([32, 68, 100, 212, 77])

@np.vectorize   
def Fahrenheit_to_Celsius(x):
    return round(((x - 32) * (5 / 9)), 2) 

result = Fahrenheit_to_Celsius(array)
np.set_printoptions(precision=2, floatmode='fixed')

print(result) 