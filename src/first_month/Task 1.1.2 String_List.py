#********STRINGS*********
#1. Write a Python program to get a string made of the first 2 and the last 2 chars from a given string.
str = "Write a Python program"
print( "#1: ", str[:2] + str[-2:] )

#2. Write a Python program to remove the nth index character from a nonempty string.
n=3
print( "#2: ", str[:n-1] + str[n:] )

#3. Write a Python program to change a given string to a new string where the first and last chars have been exchanged.
print( "#3: ",str[-1] + str[1:-1] + str[0])

#4. Write a Python function to get a string made of 4 copies of the last two characters of a specified string
print( "#4: ", str[-2:] * 4 )

#********LISTS*********
#5. Write a Python program that make a list from given string
listFromStr = list(str)
print( "#5", listFromStr )

#6. Write a Python program to print a new list which is the equivalent given list
# after removing the 0th, 4th and 5th elements.
l1 = [0,1,2,3,4,5,6,7]
print( "#6: ", l1[1:4] + l1[6:])

#7. Write a Python program which add an element to the given list
l1.append(8)
print("#7: ",  l1)

#8. Write a Python program which concat 2 lists.
l2 = ['x','y','z']
print("#8: ", l1+l2 )
