#1. Given two whole numbers - the lengths of the legs of a right-angled triangle - output its area.
base = 5;
height = 10;
area = (base*height)/2
print("Area = ", area)

#2. Input a natural number n and output its last digit.
n = 589879
print("Last digit = ", n % 10)

#3. Input a two-digit natural number and output the sum of its digits.
num = 59
digit1 = num//10
digit2 = num%10
str1 = str(59)
print("Sum =", int(str1[0]) + int(str1[1]))
print(digit1,"+",digit2, '=', digit1+digit2)

#4. You are given the first and second number in an arithmetic progression and natural number  n. Find n-th element of arithmetic progression.
a1 = 5
a2 = 8
d = a2-a1
n = 57
a57 = a1 + (n-1)*d
print("a57 = ", a57)


s = {1, 2, 3}
l = ['a','b','c','f','c','a']

print(l.index('c',2))
#print(type(l))