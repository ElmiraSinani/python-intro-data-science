#1. Write a Python program to multiply all the items in a list.
p=1
list1 = [1,2,5,10]
for x in list1:
    p *= x

print("#1: ", p)

#2. Write a Python program to get the largest number from a list.
list2 = [22,0.3,5,19,5,37,128,5,7,6]
max = list2[0]
for x in list2:
    if x>max:
        max = x

print("#2: ", max)

list2.sort()
print("#2-1: ", list2[-1])


# print maximum element
print("Largest element is:", max(list1))

#3. Write a Python program to generate and print a list except for the first 5 elements,
#   where the values are square of numbers between 1 and 30 (both included)
i = 0;
newList = [];
while i < 30:
    i += 1
    if i <= 5:
        continue
    else:
        newList.append(i ** 2)

print("#3: ", newList)

#4. Write a Python program to remove duplicates from a list
list3 = [22,5,5,19,5,37,128,5,7,6]
set1 = set(list3)
print("#4: ", list(set1))

#5. Write a Python program to find the most appeared element in a list.
mostAppeared = list3.count(list3[0])
for x in list3:
    if list3.count(x)>mostAppeared:
        mostAppeared = x

print("#5: ", mostAppeared)