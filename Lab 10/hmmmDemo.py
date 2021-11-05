# Demo of hmmm, the Harvey Mudd miniature machine
# D.Naumann 2015, rev Oct 2018
# rev Oct 2019 - Toby Dalton

import importlib
import hmmm

# When this file is ran, it runs the program assigned
# to variable RunThis (see end). Debug mode is controlled by 
# variable Mode. Read all the comments before trying it out.
# Remember to press F5 to run, after making changes.  

# Also requires hmmm.py to
# be available in the same directory as this file.

Sign = """
00 read  r1
01 calln r14 04
02 write r13
03 halt
04 setn  r13  1
05 jltzn r1  08
06 jeqzn r1  10
07 jumpr r14
08 setn  r13 -1
09 jumpn 07
10 setn r13 0
11 jumpn 07
"""


Abs = """
00 read  r1
01 calln r14 04
02 write r13
03 halt
04 copy  r13  r1
05 jgtzn r13  07
06 neg   r13  r13
07 jumpr r14
"""


Max =  """
00 read  r1
01 read  r2
02 calln r14 05
03 write r13
04 halt
05 copy  r13  r1
06 sub   r12  r1 r2
07 jltzn r12  09
08 jumpr r14
09 copy  r13  r2
10 jumpn 08
"""
 

Min =  """
00 read  r1
01 read  r2
02 calln r14 05
03 write r13
04 halt
05 copy  r13  r1
06 sub   r12  r1 r2
05 jgtzn r12  09
06 jumpr r14
07 copy  r13  r2
08 jumpn 08
"""

# Example1 is an example program that
#   1) asks the user for two inputs
#   2) computes the product of the inputs
#   3) prints out the result (with write)
#   4) stops
Example1 = """
00 read r1          # get # from user to r1
01 read r2          # ditto, for r2
02 mul r3 r1 r2     # assign r3 = r1 * r2
03 write r3         # print what's in r3
04 halt             # stop.
"""

# function call conventions:
#
# r1, r2, ...: arguments / parameters
# r13: return value
# r14: return address
# r15: stack (won't discuss)
# r12, r11, r10, ...: scratch registers
#
# mimics following python code
# def main():
#    r1 = input()
#    r2 = input()
#    r13 = mult() # always uses r1 and r2
#    r12 = r13
#    r11 = r1
#    r1 = r2
#    r2 = r11
#    r13 = mult() # we swapped r1 and r2, so that's the reverse mult
#    r13 -= r12  # r13 = r13 - r12
#    print(r13)
#
#    def mult():
#      result = r1*r2
#      return result
#
Example1plus = """
00 read r1          # get x1 from user into r1
01 read r2          # get x2 from uset into r2
02 calln r14 12     # compute x1*x2
03 copy r12 r13     # save r13 into a scratch reg
04 copy r11 r1      #
05 copy r1 r2       # swap r1 and r2 (through r11)
06 copy r2 r11      #
07 calln r14 12     # compute x2*x1 
08 sub r13 r13 r12  # checking that it's the same result
09 write r13        # expect r13 to be 0 here
10 halt             # stop.
11 nop              # begin of f()
12 mul r13 r1 r2    # assign r13 = r1 * r2
13 jumpr r14        # return to caller
"""

# N.B. Without stack (r15), we cannot make call chains...
# Make sure you understand why code below won't translate to HMMM!
# def f():
#    x = g(1)      # calln r14 <address of g()>
#    z = x+4       # execution should resume here once g() is done
#               
# def g(z):
#    w = h(z)      # calln r14 <address of h()>
#    w *= w        # execution will resume here once h() is done
#    return w      # jumpr r14  Stale value for r14!!! Loop... 
#
# def h(s):
#    return 42     # jumpr r14  Jumps to w *= w


# Example2 is an example program that
#   1) asks the user for an input
#   2) counts up from that input
#   3) keeps going and going...
Example2 = """
00 read r1          # get # from user to r1
01 write r1         # print the value of r1
02 addn r1 1        # add 1 to r1
03 jumpn 01         # jump to line 01
04 halt             # never halts! [use ctrl-c]
"""

# AbsVal is a program that asks the user for
# an input and then prints its absolute value.
AbsVal = """
00 read r1
01 jltz r1 4     # if r1 < 0 go to line 4
02 write r1      # print the absolute value
03 halt
04 setn r2 -1
05 mul r1 r1 r2  # assign r1 = r1 * -1 
06 jumpn 2       # go to line 2  
"""

# StoreLoad is an example program that
#   1) asks the user for an input
#   2) stores the value in a memory location
#   3) increments it and stores in another location
#   4) loads from that location and writes that value
# Try changing 11 to the address of an instruction!
StoreLoad = """
00 read r1         
01 storen r1 11   # put the value into mem[11]
02 addn r1 1       
03 setn r2 13 
04 storer r1 r2   # put incremented value into mem[13]
05 loadn r1 13
06 write r1       # write what was loaded
07 halt
"""

# Triangle is an example program that
#   1) asks the user for a base and height
#   2) multiplies them together
#   3) divides that by 2 (INTEGER DIVISION)
#   4) writes the 'area' of the triangle
Triangle1 = """
00 read  r1          # get base
01 read  r2          # get height
02 mul   r1 r1 r2    # b times h into r1
03 setn  r2 2
04 div   r1 r1 r2    # divide by 2
05 write r1
06 halt
"""

# Factorial returns the factorial of a number
# See if you can reason through how it works
Factorial = """
# Input: n 
# Assume: n >= 0
# Output: n!
#

# register usage: r1 for the input, r13 for the output
#
# Note that the iteration proceeds with smaller and smaller
# values multiplied into the accumulator, starting from r1
# I.e., 5! = 5 * 4 * 3 * 2 * 1 (and not as 1 * 2 * 3 * 4 * 5)

0       read    r1         # Get n, assume n>=0
1       setn    r13 1      # initialize r13
2       jeqzn   r1 6       # done if r1 is 0
3       mul     r13 r13 r1 # change r13 = r13 * r1
4       addn    r1 -1      # change r1 = r1 - 1
5       jumpn   2          # repeat
6       write   r13
7       halt
"""

# Inner product: Count the number of bit positions where the binary
# representations of x and y both have a 1 bit.
InnerProduct = """
# Input: x,y 
# Output: # of positions i such that x_i = y_i = 1, where x_i is a bit of x

# register usage: r1, r2 for input, r13 for output, r9..r12 for scratch

0       read     r1         # x
1       read     r2         # y
2       calln   r14  05     # r = ip(x,y)
3       write   r13
4       halt
5       setn    r13   0     # initialize r13
6       setn    r12   2     # constant for arithmetic operations (see below)
7       jeqzn    r1  15     # done if x reaches  0
8       mod     r11  r1 r12 # compute x % 2
9       mod     r10  r2 r12 # compute y % 2
10      mul      r9 r10 r11 # are they both one?
11      add     r13 r13  r9 # update count of bit positions where x,y both 1
12      div      r1  r1 r12 # x //= 2
13      div      r2  r2 r12 # y //= 2
14      jumpn    07         # next iteration
15      jumpr   r14         # return value of r13 to caller in r14
"""

# Hamming weight: Count the number of bit positions where the binary
# representations of x shows a 1.
HammingWeight = """
# Input: x 
# Output: # of positions i such that x_i = 1, where x_i is a bit of x

# register usage: r1 for input, r13 for output, r11,r12 for scratch

0       read    r1          # x
1       calln   r14  04     # r = hw(x)
2       write   r13
3       halt
4       setn    r13   0     # initialize r13
5       setn    r12   2     # constant for arithmetic operations (see below)
6       jeqzn    r1  11     # done if x reaches 0
7       mod     r11  r1 r12 # compute x % 2
8       add     r13 r13 r11 # update count of bit positions where x shows 1
9       div      r1  r1 r12 # x //= 2
10      jumpn    06         # next iteration
11      jumpr   r14         # return value of r13 to caller in r14
"""

def main():
    r1 = int(input())
    result = hamming_weight(r1)
    print(result)

def hamming_weight(x):
    s = 0
    while x > 0:
        a = x % 2
        s += a
        x //= 2
    return s


def main():
    r1 = int(input())
    r2 = int(input())
    result = inner_product(r1,r2)
    print(result)

def inner_product(x,y):
    s = 0
    while x > 0:
        a = x % 2
        b = y % 2
        c = a + b
        s += c
        x //= 2
        y //= 2
    return s



# Set this variable to whichever program you want to execute
# when this file is loaded.
runThis = HammingWeight

# Choose whether to use debug mode;
doDebug = True;

# When you press F5 in IDLE, the following code will
# load the assembler and simulator, then run them.
# You can interrupt with Ctrl-C; then re-start Python.

# this main functions allows you to call main() from the command line to rerun your program
def main(runArg = runThis, debugArg = doDebug):
    importlib.reload(hmmm)
    hmmm.main(runArg, debugArg)# assemble and run in one line

if __name__ == "__main__" :
    main()


