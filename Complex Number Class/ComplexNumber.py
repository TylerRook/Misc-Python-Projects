"""
Tyler Rook

Description: A script to define a class to represent a
             complex number, and code to test the class.
"""

class Complex(object):
    """
    This is a class that will represent a complex number, or
    a number of the form a + bi where a and b are real numbers
    and i is equal to the sqruare root of -1.
    """
    
    def __init__(self, a=0, b=0):
        """
        Creates a Complex object
        """
        self._a = a
        self._b = b

    def __str__(self):
        """
        Describes the Complex number
        """
        if self._a == 0 and self._b == 0:
            return "0"
        
        elif self._a == 0:
            return str(self._b)+'i'

        elif self._b == 0:
            return str(self._a)

        else:
            return "("+str(self._a)+", "+str(self._b)+"i)"

    def __add__(self, other):
        return Complex((self._a + other._a), (self._b + other._b))
        
    def __sub__(self, other):
        return Complex((self._a - other._a), ((self._b - other._b)))

    def __mul__(self, other):
        return Complex((self._a*other._a - self._b*other._b), (self._b*other._a + self._a*other._b))

    def __truediv__(self, other):
        return Complex((self._a*other._a + self._b*other._b)/(other._a**2 + other._b**2), ((self._b*other._a - self._a*other._b))/(other._a**2 + other._b**2))

    def __abs__(self):
        return (self._a**2 + self._b**2)**(1/2)

    def __eq__(self, other):
        if type(self) != type(other):
            return False
        else:
            return abs(self) == abs(other)

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        return abs(self) < abs(other)

    def __le__(self, other):
        return self < other or self == other

    def __gt__(self, other):
        return not self <= other

    def __ge__(self, other):
        return self > other or self == other
    
def main():
    input_line = input("Enter the first complex number: ")
    input_line = list(map(float,input_line.split()))
    a, b = input_line[0], input_line[1]
    c1 = Complex(a, b)
    input_line = input("Enter the second complex number: ")
    input_line = list(map(float,input_line.split()))
    a, b = input_line[0], input_line[1]
    c2 = Complex(a, b)
    
    print()
    print("c1 is", c1)
    print("c2 is", c2)
    print("|" + str(c1) + "| = " + str(abs(c1)))
    print("|" + str(c2) + "| = " + str(abs(c2)))

    print(c1, " + ", c2, " = ", c1 + c2)
    print(c1, " - ", c2, " = ", c1 - c2)
    print(c1, " * ", c2, " = ", c1 * c2)
    print(c1, " / ", c2, " = ", c1 / c2)

    print("Is c1 < c2?", c1 < c2)
    print("Is c1 <= c2?", c1 <= c2)
    print("Is c1 > c2?", c1 > c2)
    print("Is c1 >= c2?", c1 >= c2)
    print("Is c1 == c2?", c1 == c2)
    print("Is c1 != c2?", c1 != c2)
    print("Is c1 == 'Hello There'?", c1 == 'Hello There')
    print("Is c1 != 'Hello There'?", c1 != 'Hello There')

