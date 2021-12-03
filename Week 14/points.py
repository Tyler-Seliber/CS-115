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
# ** getter(s)/setter(s) (encapsulation)
# ** string methods (__repr__, __str__)
# ** basic arithmetics (equality, addition, difference)
# ** abs / distance
#
# Afterward, we'll extend this to 2D
#
# Point2D
#
# * attributes
# ** additional dimension (self.y)
#
# * methods
# ** only new things: getter/setter
# ** most of the other methods from Point will need to be
#    adjusted

import sys, math

class Point:
    def validate_params(self, val):
        return isinstance(val,int) or isinstance(val,float)

    def validate_or_signal(self, value):
        if not self.validate_params(value):
            raise TypeError('Invalid parameter (' + str(value) \
                      + ') when creating ' + str(self.__class__))
    
    def __init__(self, value=0):
        self.validate_or_signal(value)   # will quit if invalid
        self.x = value

    def __str__(self):
        return 'x='+str(self.x)

    def __repr__(self):
        return 'Point('+str(self.get_x())+')'

    def get_x(self):
        return self.x

    def set_x(self, value):
        self.validate_or_signal(value)   # will quit if invalid
        self.x = value
        
    def is_zero(self):
        return abs(self) == 0

    def __abs__(self):
        return abs(self.get_x())

    def __eq__(self, other):
        diff = self - other
        return diff.is_zero()

    def __sub__(self, other):
        # hopefully other is an instance of Point here...
        return self + (-other)

    def __neg__(self):
        neg_x = -1*self.get_x()
        return Point(neg_x)

    def __add__(self,other):
        # hopefully here other is a Point ...
        new_x = self.get_x() + other.get_x()
        return Point(new_x)

    def distance(self,other):
        # Should check other...
        return abs(self-other)

class Point2D(Point):
    def validate_params(self, values):
        return super().validate_params(values[0]) and \
               super().validate_params(values[1]) 
    
    def __init__(self, x_val=0, y_val=0):
        self.validate_or_signal((x_val, y_val))
        self.x = x_val
        self.y = y_val
        
    def get_y(self):
        return self.y

    def set_xy(self, x_val, y_val):
        self.validate_or_signal((x_val, y_val))
        self.x = x_val
        self.y = y_val
                                
    def set_x(self, x_val):
        self.set_xy(x_val, self.get_y())

    def set_y(self, y_val):
        self.set_xy(self.get_x(), y_val)

    def __str__(self):
        return super().__str__() + ",y=" + str(self.get_y())

    def __repr__(self):
        return 'Point2D(' + str(self.get_x()) \
               + ',' + str(self.get_y()) + ')'

    def __abs__(self):
        return math.sqrt(self.get_x()**2+self.get_y()**2)

    def __neg__(self):
        neg_x = -1*self.get_x()
        neg_y = -1*self.get_y()
        return Point2D(neg_x, neg_y)

    def __add__(self,other):
        # hopefully here other is a Point ...
        new_x = self.get_x() + other.get_x()
        new_y = self.get_y() + other.get_y()
        return Point2D(new_x, new_y)
