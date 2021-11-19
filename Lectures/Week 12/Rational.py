# Object Oriented Programming
class Rational:
    def __init__(self, n, d): # Constructor
        self.numerator = n
        self.denominator = d
    
    def __repr__(self):
        return "Rational(" + str(self.numerator) + ", " + str(self.denominator) + ")"
    
    def __str__(self):
        return str(self.numerator) + "/" + str(self.denominator)

