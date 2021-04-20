#1. Write a Python function, which gets 2 numbers, and return True if the second number is first number divider, otherwise False.
def checkDivider(a, b):
    if (a % b == 0):
        return True
    else:
        return False

isDivider = checkDivider(21,7)
print("#1. Is Number Divider: ", isDivider)

#2. Write a Python function, which gets a number, and return True if that number is palindrome, otherwise False
def checkPalindrome(n):
    strN = str(n)
    if (strN == strN[::-1]):
        return True
    else:
        return False

isPalindrome = checkPalindrome(123321)
print("#2. Is Number Palindrome: ", isPalindrome)

#3. Write a Python function, which gets a number, and return True if that number is prime, otherwise False.
def checkPrime(n):
    if (n<=1):
        return False
    elif (n==2):
        return True
    else:
        for i in range(2, n):
            if(n % i == 0):
                return False
        return True

isPrime = checkPrime(45)
print("#3. Is Number Prime: ", isPrime)

#4. Write a Python function, which checks if a number is perfect - that is equal to the sum of its proper positive divisors.
def checkPerfect(n):
    sum = 0
    for i in range(1, n):
        if(n % i == 0):
            sum = sum + i
    if(sum==n):
        return True
    else:
        return False

isPerfect = checkPerfect(6)
print("#4. Is Number Perfect: ", isPerfect)

#5. Write a function, which gets 2 numbers, and return their Great common divisor - https://en.wikipedia.org/wiki/Euclidean_algorithm
def getGreatCommonDivisor(a, b):
    while a!=b:
        if(a>b):
            a = a-b
        else:
            b = b-a
    return a

GreatCommonDivisor = getGreatCommonDivisor(16, 4);
print("#5. Great common divisor: ", GreatCommonDivisor)