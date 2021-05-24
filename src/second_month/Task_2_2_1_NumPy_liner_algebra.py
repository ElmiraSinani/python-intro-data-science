#
import numpy as np


# 1. Write a NumPy program to compute the multiplication of two given matrixes
def np_matrix_multiplication(m1, m2):
    return np.dot(m1, m2)


# 2. Write a NumPy program to compute the determinant of an array
def np_matrix_determinant(np_matrix):
    return np.linalg.det(np_matrix)


# 3. Write a NumPy program to compute the sum of the diagonal element of a given array
def np_diagonal_sum(np_matrix):
    return sum(np.diagonal(np_matrix))


# 4. Write a NumPy program to compute the inverse of a given matrix
def np_inverse(m):
    return np.linalg.inv(m)


# 5. Write a NumPy program to generate matrix and write it to a file, then again read from file that matrix.
def generate_matrix_write_and_read(size):
    generate_matrix = np.arange(size)
    print("Generated Matrix: \n", generate_matrix)
    np.save("generated_matrix", generate_matrix)
    read_file_inf = np.load("generated_matrix.npy")
    print("Read From File: \n", read_file_inf)


def main():
    m1 = ([1, 6, 5], [3, 4, 8], [2, 12, 3])
    m2 = ([3, 4, 6], [5, 6, 7], [6, 56, 7])

    print("#1: \n", np_matrix_multiplication(m1, m2))
    print("#2: ", np_matrix_determinant(m2))
    print("#3: ", np_diagonal_sum(m2))
    print("#4: \n", np_inverse(m2))
    print("#5: ")
    generate_matrix_write_and_read(100)


main()
