import numpy as np

v1 = np.array([1, 2])
v2 = np.array([3, 4])

print("Sum of vectors v1 and v2:", v1 + v2)

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

C = np.dot(A, B)
print("Dot product of matrices A and B:\n", C)
D = A @ B
print("Matrix multiplication of A and B:\n", D)

print("transpose of A:\n", A.T) # transpozycja zamiana wierszy na kolumny
