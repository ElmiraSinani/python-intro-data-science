#
import numpy as np
from numpy import newaxis


# 1. Գրել ծրագիր, որը բազմաչափ NumPy զանգվածում կգտնի նրա մաքսիմում և մինիմում արժեքները։
def max_and_min(n_arr):
    min_val = np.amin(n_arr)
    max_val = np.amax(n_arr)
    return {"Min": min_val, "Max": max_val}


# 2. Գրել ծրագիր, որը բազմաչափ NumPy զանգվածում կգտնի նրա մաքսիմում և մինիմում արժեքները ըստ երկրորդ սյան։
def max_and_min_by_second_col(n_arr):
    second_col = n_arr[:, 1]
    min_val = np.amin(second_col)
    max_val = np.amax(second_col)
    return {"Min": min_val, "Max": max_val}


# 3. Գրել ծրագիր, որը բազմաչափ NumPy զանգվածում կգտնի նրա մեդիանան։
def get_median(n_arr):
    return np.median(n_arr)


# 4. Ստեղծել միաչափ և երկչափ NumPy զանգվածներ և բազմապատկել իրար։
def mul_one_and_two_d_arr(n_one_d, n_two_d):
    return n_one_d*n_two_d


def main():
    n_arr = np.arange(12).reshape((3, 4))
    n_one_d = np.array([2, 3, 5, 1])
    print(n_arr)
    print("#1: ", max_and_min(n_arr))
    print("#2: ", max_and_min_by_second_col(n_arr))
    print("#3: ", get_median(n_arr))
    print("#4: \n", mul_one_and_two_d_arr(n_one_d, n_arr))

    #a1 = n_one_d[:, newaxis]
    #print(a1)
    # ten = np.arange(1, 11)
    # print(ten)
    # ten_reshaped = ten.reshape((10, 1))
    # print(ten_reshaped)
    # b = np.broadcast(ten, ten.reshape((10, 1)))
    # print(b)
    # res = ten * ten.reshape((10, 1))
    # print(res)


main()
