#1. Write a Python program to get the largest number from a list.
lst = [22,0.3,5,19,5,37,128,5,7,6]
lst.sort(reverse=True)
print(lst[0])

#2. Write a Python program to get the frequency of the given element in a list to.
print(lst.count(5))

#3. Write a Python program to remove the second element from a given list,
# if we know that the first elements index with that value is n.
list2 = ['a','s', 'k', 'n', 'j', 'h']
list2.pop(1)
print(list2)

getIndex = list2.index('n')
list2.pop(getIndex)
print(list2)
