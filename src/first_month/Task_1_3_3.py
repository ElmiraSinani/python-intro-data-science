#1. Write a Python function which returns factorial value of given number n.
def getFactorial(n):
    if n == 1:
        return 1
    else:
        return n * getFactorial(n-1)

calcFactorial = getFactorial(1)
print("#1 getFactorial", calcFactorial)

#2. Write a Python function which returns the n-th element of the fibonacci series. Fn = Fn-1 + Fn-2
def getFibonacciNum(n):
    if n<0:
        return False
    elif (n==1 or n==2):
        return n-1
    else:
        return getFibonacciNum(n-1) + getFibonacciNum(n-2)

calcFibonacci = getFibonacciNum(6)
print("#2 getFibonacciNum", calcFibonacci)

