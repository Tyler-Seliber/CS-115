# 20211129.py
#
# Antonio Nicolosi
# 21fa-cs115
#
# Demonstrate basic inheritance
#
# Abstraction for a Point class
#
# * fields/attribute
# ** one dimension, x (__init__(self), self.x)
# 
# * methods
# ** getter(s)/setter(s)
# ** string methods (__repr__, __str__)
# ** basic arithmetics (equality, addition, difference)
# ** abs / distance

import sys
import math

class Point:
    def __validate_number(value):
        return isinstance(value, int) or isinstance(value, float)
    
    def __validate(self):
        return Point.__validate_number(self.get_x())

    def __validation_error(self):
        sys.exit('Invalid Point: ' + str(self))
    
    def __init__(self, value=0):
        self.x = value
        if not self.__validate():
            self.__validation_error()

    def get_x(self):
        return self.x

    def set_x(self, value):
        self.x = value
        if not self.__validate():
            self.__validation_error()

    def __repr__(self):
        return 'Point('+str(self.get_x())+')'

    def __str__(self):
        return 'x='+str(self.get_x())

    def is_zero(self):
        return self.get_x() == 0

    def __neg__(self):
        return Point(-1*self.get_x())

    def __add__(self, other):
        # should check that other is a Point
        new_x = self.get_x() + other.get_x()
        return Point(new_x)

    def __sub__(self, other):
        # should check that other is a Point
        return self + (-other)

    def __eq__(self, other):
        diff = self - other
        return diff.is_zero()

    def __abs__(self):
        return abs(self.get_x())

    def diff(self,other):
        D = self-other
        return abs(D)
    
# After coding this class, we'll introduce another class for
# a Point2D
#
# * fields
# ** two dimensions, x and y
# *** we'll reuse (inheritance) the x from the Point class
#
# * methods
# ** adjust the same methods to the case of 2D
# *** e.g., string methods will show both coordinates

class Point2D(Point):
    def __validate(self):
        return Point.__validate_number(self.get_x()) \
               and Point.__validate_number(self.get_y())
    
    def __init__(self, x_val=0, y_val=0):
        super().__init__(x_val)
        self.y = y_val
        if not self.__validate():
            self.validation_error()

    def get_y(self):
        return self.y

P = Point()

def main():
    pass

if __name__ == '__main__':
    main()

