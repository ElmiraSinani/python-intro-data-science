import numpy as np

m1 = ([1, 6, 5],
      [3 ,4, 8],
      [2, 12, 3])

m2 = ([3, 4, 6],
      [5, 6, 7],
      [6,56, 7])

# 1. Write a NumPy program to compute the multiplication of two given matrixes
res = np.dot(m1, m2)
print("#1: \n", res)

# 2. Write a NumPy program to compute the determinant of an array
determinant = np.linalg.det(m1)
print("#2: ", determinant)

# 3. Write a NumPy program to compute the sum of the diagonal element of a given array
diagonal_elements = np.diagonal(m2)
dum_de = sum(diagonal_elements)
print("#3: ", dum_de)

# 4. Write a NumPy program to compute the inverse of a given matrix
m2_inv = np.linalg.inv(m2)
print("#4: \n", m2_inv)

# 5. Write a NumPy program to generate matrix and write it to a file, then again read from file that matrix.
generate_matrix = np.arange(100)
print("#5: \nGenerated Matrix: \n", generate_matrix)

np.save("generated_matrix", generate_matrix)

read_file_inf = np.load("generated_matrix.npy")
print("Read From File: \n", read_file_inf)
