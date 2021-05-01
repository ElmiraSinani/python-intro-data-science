class Rational:

    def __init__(self, x, y):
        self.nominator = x
        self.denominator = y

    @staticmethod
    def lcm(a, b):
        return abs(a * b) // Rational.gcd(a, b)

    @staticmethod
    def gcd(a, b):
        if b==0:
            return a
        else:
            return Rational.gcd(b, a%b)

    def __repr__(self):
        return '{}/{}'.format(self.nominator, self.denominator)

    def __add__(self, other):
        x = self.lcm(self. denominator, other.denominator)
        y = self.nominator*(x/self.denominator)+other.nominator*(x/other.denominator)
        return Rational(x,y)

    def __sub__(self, other):
        x = self.lcm(self.denominator, other.denominator)
        y = self.nominator * (x / self.denominator) - other.nominator * (x / other.denominator)
        return Rational(x, y)

    def __mul__(self, other):
        x = self.nominator*other.nominator
        y = self.denominator*other.denominator
        return Rational(x, y)

    def __div__(self, other):
        x = self.nominator * other.denominator
        y = self.denominator * other.nominator
        return Rational(x, y)

    def __eq__(self, other):
        if self.nominator/self.denominator == other.nominator/other.denominator:
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
        return Rational(self.numerator ** power, self.denominator ** power)



r1 = Rational(5, 8)
r2 = Rational(3, 2)

#print (Rational.gcd(54,24))
print (r2)
print ("__add__ ",  r1+r2)
print ("__sub__ ",  r1-r2)
print ("__mul__ ",  r1*r2)
print ("__dev__ ",  r1/r2)



