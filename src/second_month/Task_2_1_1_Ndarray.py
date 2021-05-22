# 1. Write a NumPy program to convert a list of numeric values into a one-dimensional NumPy array.
import numpy as np

list1 = [1, 5, 8, 19]
np_arr = np.array(list1)
# print(type(np_arr))
# print(np_arr.dtype)
# print(np_arr.shape)
print("#1: ", np_arr)

# 2. Write a NumPy program to create a NumPy array with values ranging from 2 to 10.
np_arr2 = np.arange(2, 11)
print("#2: ", np_arr2)

# 3. Write a NumPy program to create a null vector of size 10 and update sixth to eight values to 11.
np_arr3 = np.zeros(10)
np_arr3[5:8] = 11
print("#3: ", np_arr3)

# 4. Write a NumPy program to test whether each element of a 1-D array is also present in a second array.
arr_first = np.array([1, 2, 3])
arr_second = np.array([5, 2, 3, 4, 5, 4, 3])
print("# 4: ", np.in1d(arr_first, arr_second))

# #4 - using loop
for i in arr_first:
    if i in arr_second:
        print("True")
    else:
        print("False")
