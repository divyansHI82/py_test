# Python program for matrix operations (3x3)

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

# Transpose of A
transpose_A = [[A[j][i] for j in range(3)] for i in range(3)]

# Display results
print("Matrix A:")
for row in A: print(row)

print("\nMatrix B:")
for row in B: print(row)

print("\nAddition of A and B:")
for row in add: print(row)

print("\nSubtraction of A and B:")
for row in sub: print(row)

print("\nMultiplication of A and B:")
for row in mul: print(row)

print("\nTranspose of Matrix A:")
for row in transpose_A: print(row)

print("\nThis program is written by Divyanshi Singhal ERP id is 0221BCA150.")
