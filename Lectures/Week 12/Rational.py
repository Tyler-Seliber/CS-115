debug = True

import math, sys

class ZeroDenominatorError(ValueError):
   """Bare-bone exception class to signal zero denominators""" 
   def __init__(self):
       # Call the base class constructor with an error message
       super().__init__("Zero denominator")

class Rational:
    def validate(self):
        return isinstance(self.get_numerator(), int) \
               and isinstance(self.get_denominator(), int) \
               and 0 != self.get_denominator()

    def __signal_validation_error(self):
       # something went wrong: what to do?
       #
       # option 1: just say so, and do nothing else
       #print("something went wrong when working with fraction: " +
       #       str(self))
       # 
       # option 2: kill the program
    #    sys.exit("Rational validation error")
       #
       # option 3: raise an exception (soft kill)
       # option 3a: use a custom excpetion
       raise ZeroDenominatorError
       #
       # option 3b: use a standtard exception
       #raise ZeroDivisionError
       #

    def __init__(self, n=0, d=1):     # default arguments and named arguments
        '''
        Constructor for the Rational class.
        Uses defaul arguments:
        E.g., Rational(4) will allocate an object representing 4/1.
        E.g., Rational() will allocate an object representing  0/1.
        Notice that Python also supports named-paramteres, meaning that one can do,
        e.g., Rational(d=4) will allocate an object representing 1/4. 
        '''  
        self.numerator = n
        self.denominator = d
        if not self.validate():
            # something went wrong
            self.__signal_validation_error()

        self.__simplify()

    def get_numerator(self):
        return self.numerator

    def set_numerator(self, x):
        self.numerator = x
        if not self.validate():
            self.__signal_validation_error()

    def get_denominator(self):
        return self.denominator

    def set_denominator(self, x):
        self.denominator = x
        if not self.validate():
            self.__signal_validation_error()
        
    def __repr__ (self):
        return "Rational(" + str(self.get_numerator()) \
                + "," + str(self.get_denominator()) + ")"

    def __str__ (self):
       return str(self.get_numerator()) + "/" + str(self.get_denominator())

    def copy(self):
        return self + Rational()     # note that + will end up calling __add__

    def isZero(self):
        return 0 == self.get_numerator() 

    def __eq__(self, other):
       return self.get_numerator() * other.get_denominator() \
               == self.get_denominator() * other.get_numerator()


    def __ne__(self, other):
        return not self == other
    

#   def __lt__(self, other):
#       return self.get_numerator() * other.get_denominator() \
#               < self.get_denominator() * other.get_numerator()
#
# Consider:
#
#   Rational(1, -4) < Rational(1, 4)
#
# This would return False !!

    def __abs__(self):
        return Rational(abs(self.get_numerator()), abs(self.get_denominator()))
    
    def __sign__(self):    # note that python doesn't allow overloading of sign
        # sign computation is a mouthful in python...
        return math.copysign(1, self.get_numerator() * self.get_denominator())
 
    def __lt__(self, other):
        # take sign and absolute value into account separately
        signSelf,  absSelf  = self.__sign__(), abs(self)
        signOther, absOther = other.__sign__(), abs(other)
        return signSelf < signOther \
            or signSelf * absSelf.get_numerator() * absOther.get_denominator() \
               < signOther * absOther.get_numerator() * absSelf.get_denominator()
               
    def __le__(self, other):
        return self == other or self < other
               
    def __gt__(self, other):
        return not self <= other
               
    def __ge__(self, other):
        return not self < other
               
    def __add__(self, other):
        newDenominator = self.get_denominator()*other.get_denominator()
        newNumerator = self.get_numerator()*other.get_denominator() \
                       + self.get_denominator()*other.get_numerator()
        res = Rational(newNumerator, newDenominator)
        res.__simplify()
        return res

    def __mul__(self, other):
        newDenominator = self.get_denominator()*other.get_denominator()
        newNumerator = self.get_numerator()*other.get_numerator()
        res = Rational(newNumerator, newDenominator)
        res.__simplify()
        return res

    def __truediv__(self, other):
        # dunder operator identifier for float division ('/')
        return self * other.inverse()

    def inverse(self):
        res = Rational(self.get_denominator(), self.get_numerator())
        if not res.validate():
            sys.exit()
#            raise ZeroDenominatorError
        return res
    
    def __neg__(self):
        return Rational(- self.get_numerator(),self.get_denominator())

    def __sub__(self, other):
        return self + (-other)

    def __int__(self):        # As an alternative, one could choose to round toward 0
        return self.get_numerator()//self.get_denominator()

    def  __float__(self):
        return self.get_numerator()/self.get_denominator()
    
    def __simplify(self):
        g = Rational.gcd(self.get_denominator(), self.get_numerator())
        self.set_denominator(self.get_denominator() //  g)
        self.set_numerator(self.get_numerator()  // g)
        
    def gcd(a,b):
        a,b = abs(a),abs(b)
        while 0 < b:
            r = a % b
            a = b
            b = r

        return a

    # feel free to skip the following method
    
    def sqrt(self, inv_tolerance=1000):
        """
        Compute an approximate square root.
        Use the babylonian algorithm till the result is within
        1/tolerance of the true value
        """
        tolerance = Rational(1, inv_tolerance)
        h = self.copy()
        w = Rational(1)

        if debug: print(h-w)
        while not (-tolerance < h - w < tolerance):
            h = Rational(1, 2) * (h + w) 
            w = self / h
            if debug: print(h-w); print(float(h))

        return h

## __name__
## '__main__'

def main():
    f1 = Rational(2, 4)
    f2 = Rational(-1, -2)
    f3 = Rational(4, 6)
    f4 = f3 - f1
    print('f4 = ' + str(f4))


if __name__ == '__main__':
    main()
