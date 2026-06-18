import numpy as np


matrix  = np.array([
[1,2,3],
[2,3,4]

])

print("\n\n Matrix \n")
print(matrix)

print("\n Print Shape: ", matrix.shape)
print("\n Print Size: ", matrix.size)
print("\n Print Dimenstion: ", matrix.ndim)


print("\n Element at [0,0]:", matrix[0, 0])
print("\n Element at [0,2]:", matrix[0, 2])
print("\n Element at [1,1]:", matrix[1, 1])



print("\n First Row:", matrix[0])
print("\n Second Row:", matrix[1])

print("\n First Column:", matrix[:, 0])
print("\n Second Column:", matrix[:, 1])




matrix1  = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])


print("\n\n Matrix -1 \n")
print(matrix1)


print("\n Print Shape: ", matrix1.shape)
print("\n Print Size: ", matrix1.size)
print("\n Print Dimenstion: ", matrix1.ndim)


print("\n Element 50               :", matrix1[1,1])
print("\n Element in 3rd row       :", matrix1[2])
print("\n Element at first column  :", matrix1[:, 0])






