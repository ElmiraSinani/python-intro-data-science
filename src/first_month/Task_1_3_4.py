#Write a Python function, which Implements the Euler function.
#Euler function is return a count of numbers not great than N, which are mutually simple with N.
#Example  φ(6)=2, as only 1 and 5 from 1,2,3,4,5 are mutually simple with 6. Write a function which returns a count of numbers mutually simple with given N.


#2. Ticket numbers usually consist of an even number of digits. A ticket number is considered lucky if the sum of the first half of the digits is equal to the sum of the second half.
#Given a ticket number n, determine if it's lucky or not.
#For n = 1230, the output should be -> isLucky(n) = true;
#For n = 239017, the output should be -> #isLucky(n) = false.
def isLucky(n):
     strNum = str(n)
     sum1 = 0
     sum2 = 0
     for i in range(0, len(strNum)):
         if i<int(len(strNum))/2:
            sum1 = sum1 + int(strNum[i])
         else:
            sum2 = sum2 + int(strNum[i])
     if sum1==sum2:
        return True
     return False

print( isLucky(239017) )

#3. The robot is standing on a rectangular grid and is currently located at the point (X0, Y0). The coordinates are integers. It receives N remote commands(list with n elements each of them is a command). Each command is one of : up, down, left, right. Upon receiving a correct command, the robot moves one unit in the given direction. If the robot receives an incorrect command, it simply ignores it. Where will the robot be located after following all the commands?

#4. Write a python function, which returns the sum of digits of given number N.
def sumOfDijits(n):
    strNum = str(n)
    sum = 0
    for i in range(0, len(strNum)):
        sum = sum + int(strNum[i])
    return sum

print(sumOfDijits(1234))


#5. Write a python program to find the next smallest palindrome of a specified number. For example, for 119 next palindrome is 121.
def nextSmallestPalindrom(n):
    while True:
        n = n + 1;
        strNum = str(n)
        if strNum == strNum[::-1]:
            return strNum

print(nextSmallestPalindrom(119))

def prevSmallestPalindrom(n):
    for i in range(-n, 0):
        strNum = str(abs(i))
        #print(strNum)
        if strNum == strNum[::-1]:
            return strNum

print(prevSmallestPalindrom(119))