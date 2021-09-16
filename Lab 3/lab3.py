##########################################
# Name: Tyler Seliber
# Pledge: I pledge my honor that I have abided by the Stevens Honor System
##########################################

# Import reduce from the functools package
from functools import reduce

#######################################################################################
# Task 1: Use reduce to determine if all elements in a boolean list are true
def all_true(lst):

    def both_true(a,b):
        return a and b

    return reduce(both_true, lst)


#######################################################################################
# Task 1.1: Use reduce to determine if AT LEAST one element in a boolean list is true
# Hint: Should be very similar to the above function
def one_true(lst):
    
    def has_true(a,b):
        return a or b

    return reduce(has_true, lst)

#######################################################################################
# Task 2: Use map and reduce to return how many elements are True in a boolean list
def count_true(lst):
    
    # Convert booleans to integers
    def convert_bool(a):
        return int(a)
    
    # Sum the converted integers
    def count_bool(a,b):
        return a + b
    
    return reduce(count_bool, map(convert_bool, lst))


# This function is provided for you
# Gets a list of strings through the command line
# Input is accepted line-by-line
def getInput():
    lst = []
    txt = input()

    while(len(txt) != 0):
        lst.append(txt)
        txt = input()

    return lst

# Task 3: Get the longest string in the list using map and reduce, and print it out
# 'strings' is a list of input strings e.g. [ 'hello', 'world' ]
# Hint: The 'map' part of your program should take a string s into a length-2 list [len(s), s].
def getLongestString():
    strings = getInput()

    # Get length of each input string
    def char_count(s):
        return [len(s), s]

    # Return larger of two string lengths
    def find_largest(a,b):
        return max(a,b)

    # Return the second element of the list returned from find_largest() ('reduce' part), which is the longest string
    return reduce(find_largest, map(char_count, strings))[1]


# Test code

# test_list = [True,True,True,False,True,False]

# Task 1
# print(all_true(test_list))

# Task 1.1
# print(one_true(test_list))

# Task 2
# print(count_true(test_list))

# Task 3
# print(getLongestString())