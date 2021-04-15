# 1. Write a Python program to get the largest number from a list.
lst = [22, 0.3, 5, 19, 5, 37, 128, 5, 7, 6, 5]
lst.sort(reverse=True)
print("#1 ", lst[0])

# 2. Write a Python program to get the frequency of the given element in a list to.
print("#2 ", lst.count(5))

# 3. Write a Python program to remove the second element from a given list,
# if we know that the first elements index with that value is n.
list2 = [0, 2, 5, 1, 0, 8, 9, 3, 0]
getIndex = list2.index(0)
list2.pop(getIndex+1)
print("#3 ", list2)