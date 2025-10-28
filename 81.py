# Python program to perform matrix operations with and without NumPy

# -------- WITHOUT NUMPY --------
A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

B = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

# Addition
add = [[A[i][j] + B[i][j] for j in range(3)] for i in range(3)]

# Subtraction
sub = [[A[i][j] - B[i][j] for j in range(3)] for i in range(3)]

# Multiplication
mul = [[sum(A[i][k] * B[k][j] for k in range(3)) for j in range(3)] for i in range(3)]

# Transpose
transpose_A = [[A[j][i] for j in range(3)] for i in range(3)]

print("---- WITHOUT NUMPY ----")
print("Matrix A:")
for row in A: print(row)
print("\nMatrix B:")
for row in B: print(row)
print("\nAddition:\n", add)
print("\nSubtraction:\n", sub)
print("\nMultiplication:\n", mul)
print("\nTranspose of A:\n", transpose_A)


# -------- WITH NUMPY --------
import numpy as np

A_np = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]])

B_np = np.array([[9, 8, 7],
                 [6, 5, 4],
                 [3, 2, 1]])

add_np = A_np + B_np
sub_np = A_np - B_np
mul_np = np.dot(A_np, B_np)
transpose_np = A_np.T

print("\n---- WITH NUMPY ----")
print("Matrix A:\n", A_np)
print("\nMatrix B:\n", B_np)
print("\nAddition:\n", add_np)
print("\nSubtraction:\n", sub_np)
print("\nMultiplication:\n", mul_np)
print("\nTranspose of A:\n", transpose_np)

print("\nThis program is written by Divyanshi Singhal ERP id is 0221BCA150.")
