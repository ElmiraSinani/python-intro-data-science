#!/usr/bin/env python
# -*- coding: utf-8 -*-
from CustomExceptions import InvalidInputError


class Rational:
    def __init__(self, x, y):
        try:
            if y == 0:
                raise InvalidInputError("Y can't be zero", y)
            else:
                gcd = Rational.gcd(x, y)
                self.nominator = int(x // gcd)
                self.denominator = int(y // gcd)
        except InvalidInputError as e:
            print("CustomValueError Exception!", e)

    @staticmethod
    def lcm(a, b):
        return abs(a * b) // Rational.gcd(a, b)

    @staticmethod
    def gcd(a, b):
        if b == 0:
            return a
        else:
            return Rational.gcd(b, a % b)

    def __repr__(self):
        return '{}/{}'.format(self.nominator, self.denominator)

    def __add__(self, other):
        x = self.lcm(self. denominator, other.denominator)
        y = self.nominator*(x/self.denominator)+other.nominator*(x/other.denominator)
        return Rational(y, x)

    def __sub__(self, other):
        x = self.lcm(self.denominator, other.denominator)
        y = self.nominator * (x / self.denominator) - other.nominator * (x / other.denominator)
        return Rational(int(y), int(x))

    def __mul__(self, other):
        x = self.nominator*other.nominator
        y = self.denominator*other.denominator
        return Rational(x, y)

    def __truediv__(self, other):
        x = self.nominator * other.denominator
        y = self.denominator * other.nominator
        return Rational(x, y)

    def __eq__(self, other):
        if self.nominator == other.nominator and self.denominator == other.denominator:
            return True
        return False

    def __gt__(self, other):
        if self.nominator / self.denominator > other.nominator / other.denominator:
            return True
        return False

    def __ge__(self, other):
        if self.nominator / self.denominator >= other.nominator / other.denominator:
            return True
        return False

    def __lt__(self, other):
        if self.nominator / self.denominator < other.nominator / other.denominator:
            return True
        return False

    def __le__(self, other):
        if self.nominator / self.denominator <= other.nominator / other.denominator:
            return True
        return False

    def __pow__(self, power, modulo=None):
        return Rational(self.nominator ** power, self.denominator ** power)



r1 = Rational(-1, 0)
r2 = Rational(1, -5)
print(r1)
print(r2)
# print (Rational.gcd(54,24))
# print (Rational.lcm(54,24))

print ("__add__ ",  r1+r2)
print ("__eq__ ",  r1==r2)
print ("__sub__ ",  r1-r2)
print ("__mul__ ",  r1*r2)
print ("__dev__ ",  r1/r2)
print("__pow__ ", pow(r1, 2))




# Class - Rational
#
# Data members -
# numerator - integer(համարիչ)
# denumerator - integer(հայտարար)
#
# Data Methods
# Constructor - not only assign values to data member, but also simplify,
# For example if we have an object obj = Rational(6,8), should create an object with values (3,4). Use GCD algorithm, for simplifying.
#
# Ոչ միայն պետք է ուղղակի վերագրի համարիչի և հայտարարի արժեքները, այլ նաև պետք է պարզեցնի այն,
# օրինակ Rational(6,8) ֊ի դեպքում պետք է սարքի օբյեկտ համապատասխան (3,4) արժեքներով։
# Պարզեցման համար օգտվել ամենամեծ ընդհանուր բաժանարարի ֆունկցիայից։
# 	__repr__
# 	__add__
# 	__sub__
# 	__mul__
# 	__div__
# 	__eq__
# 	__gt__
# 	__gte__
# 	__lt__
# 	__lte__
# 	__pow__
