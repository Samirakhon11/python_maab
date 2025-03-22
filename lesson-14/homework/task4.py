import numpy as np

X = np.array([
    [10, -2, 3], 
    [-2, 8, -1], 
    [3, -1, 6]
    ])
Y = np.array([12, -5, 15])  

if np.linalg.det(X) == 0:
    print("This equation has no unique solution!")
else:
    result = np.linalg.solve(X, Y) 
    print(result) 