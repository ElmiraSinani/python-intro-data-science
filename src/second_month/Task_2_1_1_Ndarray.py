#
import numpy as np


# 1. Write a NumPy program to convert a list of numeric values into a one-dimensional NumPy array.
def list_to_np_array(lst):
    return np.array(lst)


# 2. Write a NumPy program to create a NumPy array with values ranging from 2 to 10.
def np_array_with_range(start, end):
    return np.arange(start, end)


# 3. Write a NumPy program to create a null vector of size 10 and update sixth to eight values to 11.
def np_zero_arr(size):
    np_arr = np.zeros(size)
    np_arr[5:8] = 11
    return np_arr


# 4. Write a NumPy program to test whether each element of a 1-D array is also present in a second array.
def np_test_arr_in(arr1, arr2):
    return np.in1d(arr1, arr2)


# 4 - using loop
def np_test_arr_in_1(arr1, arr2):
    res = []
    for i in arr1:
        if i in arr2:
            res.append(True)
        else:
            res.append(False)
    return res


def main():
    list1 = [1, 5, 8, 19]
    arr_first = np.array([1, 2, 8])
    arr_second = np.array([1, 2, 3, 4, 5, 2, 3])
    print("#1: ", list_to_np_array(list1))
    print("#2: ", np_array_with_range(2, 8))
    print("#3: ", np_zero_arr(10))
    print("# 4: ", np_test_arr_in(arr_first, arr_second))
    print("# 4 - 1: ", np_test_arr_in_1(arr_first, arr_second))


main()
