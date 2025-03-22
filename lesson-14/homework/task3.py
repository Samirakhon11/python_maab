import numpy as np

X = np.array([
    [4, 5, 6],
    [3, -1, 1],
    [2, 1, -2]
    ])
Y = np.array([7, 4, 5]) 

if np.linalg.det(X) == 0:
    print("This equation has no unique solution!")
else:
    result = np.linalg.solve(X, Y) 
    print(result) 