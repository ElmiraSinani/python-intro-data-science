# 1. Write a Python program to get the largest number from a list.
lst = [22, 0.3, 5, 19, 5, 37, 128, 5, 7, 6, 5]
lst.sort(reverse=True)
print("#1 ", lst[0])

# 2. Write a Python program to get the frequency of the given element in a list to.
print("#2 ", lst.count(5))

# 3. Write a Python program to remove the second element from a given list,
# if we know that the first elements index with that value is n.
list2 = [5, 4, 'A', 3, 4, 5, 6, 'A', 7, 2, 8, 1, 9, 2, 10, 2, 11]
print(list2)
# firstIndexA = 2
firstIndexA = list2.index('A')
slicedList = list2[firstIndexA+1:]
elmCount = len(list2[:firstIndexA+1])
secondIndexA = slicedList.index('A')
list2.pop(secondIndexA+elmCount)
print(list2)

