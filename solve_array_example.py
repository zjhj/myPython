import numpy as np

A = np.mat("1 -2 1;0 2 -8;-4 5 9")
b = np.array([0, 8, -9])
x = np.linalg.solve(A, b)
print "Solution", x
