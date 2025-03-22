import numpy as np

array1 = np.array([2, 3, 4, 5])
array2 = np.array([1, 2, 3, 4])

@np.vectorize
def calculate_power(arr, power):
    return arr ** power

while True:
    try:
        power = int(input("Enter a number for power:"))
        if power < 0:
            raise ValueError("Enter a positive number only") 
        break
    except ValueError as e:
        print(e) 

result1 = calculate_power(array1, power)
result2 = calculate_power(array2, power) 

print(result1)
print(result2) 