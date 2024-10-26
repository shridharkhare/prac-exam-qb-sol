import numpy as np

row = int(input("Enter the number of rows: "))
col = int(input("Enter the number of columns: "))

shape_mat = (row, col)

mat1 = np.zeros(shape_mat, dtype=int)
mat2 = np.zeros(shape_mat, dtype=int)

print("Enter the elements of the first matrix:")
for i in range(row):
    for j in range(col):
        mat1[i][j] = int(input())

print("Enter the elements of the second matrix:")
for i in range(row):
    for j in range(col):
        mat2[i][j] = int(input())

print("The sum of the two matrices is:")
print(mat1 + mat2)

print("The multiplication of the two matrices is:")
print(np.matmul(mat1, mat2))
