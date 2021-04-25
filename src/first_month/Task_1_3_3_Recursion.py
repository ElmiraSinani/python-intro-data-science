#1. Write a Python function which returns factorial value of given number n.
def getFactorial(n):
    if n == 1:
        return 1
    else:
        return n * getFactorial(n-1)

calcFactorial = getFactorial(6)
print("#1.1 getFactorial", calcFactorial)

def getFactorialFor(n):
    f = 1
    for i in range(1, n+1):
        f = f * i
    return f

print("#1.2 getFactorialFor", getFactorialFor(6))

def getFactorialWhile(n):
    i = 1; f = 1;
    while (i<=n):
        f = f * i
        i += 1
    return f

print("#1.3 getFactorialWhile", getFactorialWhile(5))


#2. Write a Python function which returns the n-th element of the fibonacci series. Fn = Fn-1 + Fn-2
def getFibonacciNum(n):
    if n<0:
        return False
    elif (n==1 or n==2):
        return n-1
    else:
        return getFibonacciNum(n-1) + getFibonacciNum(n-2)

calcFibonacci = getFibonacciNum(5)
print("#2.1 getFibonacciNum", calcFibonacci)

def getFibonacciNumFor(n):
    f = [0, 1]
    for i in range(2, n + 1):
        f.append(f[i - 1] + f[i - 2])
    return f[n-1]

print("#2.2 getFibonacciNumFor", getFibonacciNumFor(5))

def getFibonacciNumWhile(n):
    f = [0, 1]
    i=2
    while (i <= n):
        f.append(f[i - 1] + f[i - 2])
        i += 1
    return f[n-1]

print("#2.3 getFibonacciNumFor", getFibonacciNumWhile(5))



