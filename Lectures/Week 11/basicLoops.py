#
# 21fa-cs115bc
#
# basicLoops.py
#
# A.Nicolosi
# 20211112
#
# Practice with loops.

# In assembly, loops are usually based on the exit condition:
#
# conditional jump out of the loop (exit condition)
# body of the loop
# ...
# end of loop body
# jumpn back to the head of the loop
# out-of-the-loop
#
# In Python, while loops (a.k.a. undefinite loops) are based on
# a 'guard'  (condition must be true for loop to continue)
#
# while <guard>:
#    body of the loop
#    ...
#    end of the loop
# out-of-the-loop


debug = True

def whileFactorial(n):   # think of n as 5
    accumulator = 1
    while n>0:        # remember, python uses the loop condition (not exit)
        accumulator *= n
        n -= 1
    return accumulator

def whileFibonacci(n):
    if n<2:
        value=n
    else:
        prev=1
        value=1
        while n>2:
            next_value = prev + value
            prev = value
            value = next_value
            n -= 1
    return value

# demonstration of the break statement
def input_loop():
    while True:
        ans =  input("Do you want to keep going?\n")
        if ans in ['n', 'N', 'no', 'No', 'NO']:   # exit condition
            break

# for loop (a.k.a.) definite loops
# i.e., you know ahead of time how many times to loop
# for: loop variable (will take in turn all values from a given "iterable"
def forFactorial(n):
    accumulator = 1
    for i in range(2,n+1):
        accumulator *= i

    return accumulator

def forDemo(limit, brake):
    for i in range(limit):
        if debug: print("inside, i=",i)
        if brake == i:
            break
    print("outside, i=", i)

def whileDemo(limit, brake):
    i = 0
    while i < limit:
        if debug: print("inside, i=", i)
        if brake == i:
            break
        i += 1
    print("outside, i=", i)

def f():
    L = [1, 2, 3, 4]
    g(L)
    return L

def g(LL):
    LL[0] = 42


# Three average problem
# Given a list L, compute a new list where the first and last
# items are unchanged, and every internal item is replaced with
# the average of its value with the values immediately before and
# after it.
#
# E.g., [] --> []
# E.g., [10] --> [10]
# E.g., [10, 20] --> [10, 20]
# E.g., [3, 4, 5, 6] -->  [3.0, 4.0, 5.0, 6.0]
# E.g., [3, 9, 12, 9] --> [3.0, 8.0, 10.0, 9.0]
# E.g., [3, 8, 10, 9] --> [3.0, 7.0, 9.0, 9.0]

def threeAverageWrong(L):
    newL = L   # XXX this doesn't work
    for i in range(1, len(newL)-1):
        newL[i] = (L[i-1] + L[i] + L[i+1]) / 3.0
    return newL
    
def threeAverageL2R(L):
    # First, copy the input list L into a new list
    #
    # * WRONG approach: 
    # newL = L      # doesn't work!  Shallow copy
    #
    # * working approach: copy items from L one by one
    newL = []
    for i in range(len(L)):
        newL += [float(L[i])]  # turn to float while making copy

    # * better approach: copy through map with float-convertion
    #newL = list(map(lambda x: x, L))

    # Next, iterate through the new list
    #
    # for each entry i, except for first and last,
    # average it with entries (i-1) and (i+1)
    for i in range(len(newL)):
        if 0 == i or len(newL)-1 == i:
            continue      # goes straight to the next iteration       
        newL[i] += L[i-1]
        newL[i] += L[i+1]
        newL[i] /= 3.0        # notice the decimal point ('.')
                                  # not strictly needed in Python3, but
                                  # makes for good style, b/c in other
                                  # programming languages it ensures
                                  # 'true' (rather than integer) division
        #
        # above conditional statement could have been written with
        # flipped condition to demoonstrate use of 'continue'
                                  
    return newL

def threeAverageWithMap(L):
    # functional approach to implementing the 3-average problem
    #
    # idea: compute three versions of the input list:
    #
    # * left-shifted list, obtained skipping the first 2 items
    # * trimmed list, obtained trimming first and last 
    # * right-shifted list, obtained skipping the last 2 items
    #
    # For example, if L is [1, 2, 3, 4, 5, 6], the three lists are:
    #
    # * Left-shifted:
    #
    #   [1, 2, 3, 4, 5, 6 ]
    #         /  /  /  /
    #        /  /  /  /
    #       /  /  /  /
    #      /  /  /  /
    #     /  /  /  /
    #   [3, 4, 5, 6]
    #
    #
    # * End-trimmed:
    # 
    #   [1, 2, 3, 4, 5, 6 ]
    #       |  |  |  |
    #       |  |  |  |
    #      [2, 3, 4, 5]
    #
    #
    # * Right-shifted:
    # 
    #   [1, 2, 3, 4, 5, 6 ]
    #     \  \  \  \  
    #      \  \  \  \  
    #       \  \  \  \  
    #        \  \  \  \  
    #         \  \  \  \  
    #         [1, 2, 3, 4]
    #
    leftShifted = L[2:]
    endTrimmed = L[1:-1]
    rightShifted= L[:-2]

    # The result can then be computed by averaging the three
    # lists entry-wise, and then prepending/appending the ends:
    #
    # |  [3, 4, 5, 6]  |
    # |  [2, 3, 4, 5]  |
    # |  [1, 2, 3, 4]  |
    # |  ------------  |
    # v  [2, 3, 4, 5]  v
    #
    # [1, 2, 3, 4, 5, 6]
    #
    averaged = list(map(lambda x, y, z: (x + y + z)/3., 
                        leftShifted, 
                        endTrimmed,
                        rightShifted)) 

    return [float(L[0])] + averaged + [float(L[-1])]
