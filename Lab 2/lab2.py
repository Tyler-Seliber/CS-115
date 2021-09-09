import math

# Name: Tyler Seliber
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.

# All of the functions with the solve prefix are to be implemented using four fours and
# basic math operations to equal the number in the function title. The basic operations are
# +, -, *, /, and parentheses.
# To fill the function out, replace the 0 with your expression so that the function will return
# the number in the function title

# As an example the solution for 12 and a way to test it is given below
# If your output has a decimal in the solution, it will not be counted against you,
# but if you'd like to remove it use // for division


def solve_12():
    return 4 * (4 - 4 // 4)


print(solve_12())  # Will print 12


def solve_0():
    return (4 - 4) + (4 - 4)


def solve_1():
    return (4 // 4) * (4 // 4)


def solve_2():
    return (4 // 4) + (4 // 4)


def solve_3():
    return (4 + 4 + 4) // 4


def solve_4():
    return 4 + ((4 - 4) // 4)


def solve_5():
    return (4 * 4 + 4) // 4


def solve_6():
    return ((4 + 4) // 4) + 4


def solve_7():
    return (4 + 4) - (4 // 4)


def solve_8():
    return (4 * 4) - (4 + 4)


def solve_9():
    return (4 + 4) + (4 // 4)

# Test each function
# print('solve_0: ' + str(solve_0()))
# print('solve_1: ' + str(solve_1()))
# print('solve_2: ' + str(solve_2()))
# print('solve_3: ' + str(solve_3()))
# print('solve_4: ' + str(solve_4()))
# print('solve_5: ' + str(solve_5()))
# print('solve_6: ' + str(solve_6()))
# print('solve_7: ' + str(solve_7()))
# print('solve_8: ' + str(solve_8()))
# print('solve_9: ' + str(solve_9()))


# To solve this one you're allowed to use any operation you'd like
# This includes factorials, square roots, and concatenation (Using two 4s to make 44)
# The math library has already been imported so you can use math.sqrt(n) for square roots
# and math.factorial(n) for factorials
def solve_10():
    return math.trunc(math.sqrt(4) * 4 + 4 - math.sqrt(4))

# Test solve_10()
# print('solve_10: ' + str(solve_10()))

# The following problems are to act as introductions to lists.
# All of them will use a list, titled lst, in the function which
# you can assume will not produce an error

# Simple tests are given below each function
example_lst = [1, 2, 3, 4, 5]

# Returns the first element of a list


def get_first(lst):
    return lst[0]


print(get_first(example_lst))  # Prints 1


# Returns the last element of a list
def get_last(lst):
    return lst[-1]


print(get_last(example_lst))  # Prints 5


# Returns a list containing all elements except the first
# Hint: use list slices
def remove_first(lst):
    return lst[1:]


print(remove_first(example_lst))  # Prints [2, 3, 4, 5]
