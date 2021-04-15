#1. Given two whole numbers - the lengths of the legs of a right-angled triangle - output its area.
base = 5;
height = 10;
area = (base*height)/2
print("#1 Area = ", area)

#2. Input a natural number n and output its last digit.
n = 589879
print("#2 Last digit = ", n % 10)

#3. Input a two-digit natural number and output the sum of its digits.
num = 59
digit1 = num//10
digit2 = num%10
print("#3 2. Sum =", digit1+digit2)

str1 = str(num)
print("#3 1. Sum =", int(str1[0]) + int(str1[1]))


#4. You are given the first and second number in an arithmetic progression and natural number  n. Find n-th element of arithmetic progression.
a1 = 5
a2 = 8
d = a2-a1
n = 57
a57 = a1 + (n-1)*d
print("#4 a57 = ", a57)

