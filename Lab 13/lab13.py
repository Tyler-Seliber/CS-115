# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Name    : Tyler Seliber
# Pledge  : I pledge my honor that I have abided by the Stevens Honor System.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#
# 21fa-cs115bc
#
# lab13.py
#
# A.Nicolosi
# 20211201
#
# Practice with classes.

# TODO: Write a bare-bone class InvalidDateError that inherits from ValueError
# Your constructor should allow for up to three argument (for the month,
# day, and year).  Hint: recall the syntax for default parameter values.

class InvalidDateError(ValueError):
    '''Raised when an invalid date is entered.'''
    def __init__(self, month, day, year):
        self.month = month
        self.day = day
        self.year = year
        super().__init__(f'{month}/{day}/{year} is an invalid date.')

# Fill in the missing part in the class Date below
class Date:
    '''
    Date abstraction

    Demonstrate getter/setter methods and operator overloading
    '''

    daysInMonth = [31,          # not really using index 0 (dec of prev year)
                   31, 28, 31,  # jan, (non-leap) feb, mar
                   30, 31, 30,  # apr, may, jun
                   31, 31, 30,  # jul, aug, sep
                   31, 30, 31]  # oct, nov, dec

    def isLeapYear(year):
        # Every fourth year is a leap year,
        # except that every one-hundreth year it isn't,
        # but every four-hundreth year is a leap year after all!
        #
        result = False
        if (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)):
            result = True
        return result


    def __init__(self, month=1, day=1, year=1970):
        # Call self.validate to ensure that the parameters
        # make a valid date.  Raise an InvalidDateError if not.
        # If all is good, initialize the attributes _month, _day, and
        # _year
      
        if self.validate_params(month, day, year):
            self.month = month
            self.day = day
            self.year = year
        else:
            raise InvalidDateError(month, day, year)

    def __repr__(self):
        # Make sure to return a string that looks like a valid
        # call to the class constructor
        # Ex: Date(12, 31, 2021)
        
        return "Date(" + str(self.get_month()) + ", " + str(self.get_day()) + ", " + str(self.get_year()) + ")"

    def __str__(self):
        # Return a string in the format mm/dd/yyyy
        
        return str(self.get_month()) + "/" + str(self.get_day()) + "/" + str(self.get_year())

    def _validateCheckFeb29(m, d, y):
        return 2 == m and 29 == d and Date.isLeapYear(y)

    def validate_params(self, m, d, y):
        # Return True if m, d, y represent a valid date
        # Start by checking if that's a valid Feb 29 (see
        # helper above); then check if d is a valid day
        # in month m

        if Date._validateCheckFeb29(m, d, y):
            return True
        if y < 1 or m < 1 or m > 12 or d < 1 or d > Date.daysInMonth[m]:
            return False
        return True

    # Write getters and setters
    # TODO: get_month, get_day, get_year, set_month, set_day, set_year
    # NB: Setter should check that the resulting date is valid
    # *before* affecting the change
    
    def get_month(self):
        return self.month

    def get_day(self):
        return self.day

    def get_year(self):
        return self.year

    def set_month(self, month):
        if self.validate_params(month, self.day, self.year):
            self.month = month
        else:
            raise InvalidDateError(month, self.day, self.year)

    def set_day(self, day):
        if self.validate_params(self.month, day, self.year):
            self.day = day
        else:
            raise InvalidDateError(self.month, day, self.year)

    def set_year(self, year):
        if self.validate_params(self.month, self.day, year):
            self.year = year
        else:
            raise InvalidDateError(self.month, self.day, year)

    # Date arithmetic!

    def __eq__(self, other):
        return (self.get_month() == other.get_month() and self.get_day() == other.get_day() and self.get_year() == other.get_year())

    def __ne__(self, other):
        return not (self == other)
    
    def __lt__(self, other):
        if self.get_year() < other.get_year():
            return True
        elif (self.get_month() < other.get_month()) and (self.get_year() == other.get_year()):
            return True
        elif (self.get_day() < other.get_day()) and (self.get_month() == other.get_month()):
            return True
        else:
            return False

    def __ge__(self, other):
        return not (self < other)

    def __le__(self, other):
        return (self < other or self == other)

    def __gt__(self, other):
        return not (self <= other)

    def __add__(self, deltaInDays):
        '''Computes the date following `self` by the specified number of days'''
        newDay = Date(self.get_month(), self.get_day(), self.get_year())
        if newDay.validate_params(newDay.get_month(), newDay.get_day() + deltaInDays, newDay.get_year()):
            newDay.set_day(newDay.get_day() + deltaInDays)
            return newDay
        days_remaining_in_month = Date.daysInMonth[self.get_month()] - self.get_day()
        # Add an extra day if it is a leap day
        if newDay.get_month() == 2 and Date.isLeapYear(newDay.get_year()):
            days_remaining_in_month += 1
        if (newDay.get_month() >= 12):
            newDay.set_month(1)
            newDay.set_year(self.get_year() + 1)
        else: 
            newDay.set_month(self.get_month() + 1)
        newDay.set_day(1)
        return newDay.__add__(deltaInDays - days_remaining_in_month - 1)
        
