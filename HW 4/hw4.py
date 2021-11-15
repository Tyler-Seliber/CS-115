# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Name    : Tyler Seliber
# Pledge  : I pledge my honor that I have abided by the Stevens Honor System.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

from importlib import reload as Rfrsh
import hmmm

# Fibonacci! You've already done it in Lab 9
# Now however, you are to do hmmmonacci with
# recursion, & you MUST do so for any credit
# The tests are still the same as from Lab 9
# Tests: f(2) = 1, f(5) = 5, f(9) = 34
RecFibSeq = """ # You may not need all lines
00 setn r15 60 # answer = fibonacci(n)
01 read r1 # n = input
02 nop
03 nop
04 calln r14 7 # answer = fibonacci(n)
05 write r13 # print answer
06 halt
07 jnezn r1 10 # if n == 0
08 setn r13 0 # res = 0
09 jumpr r14 # return res
10 addn r1 -1 # n = n - 1
11 jnezn r1 14 # if n == 1
12 setn r13 1 # res = 1
13 jumpr r14 # return res
14 pushr r1 r15
15 pushr r14 r15
16 calln r14 7 # res = fibonacci(n)
17 popr r14 r15
18 popr r1 r15
19 copy r12 r13
20 addn r1 -1 # n = n - 1
21 pushr r1 r15
22 pushr r12 r15
23 pushr r14 r15
24 calln r14 7 # res2 = fibonacci(n)
25 popr r14 r15
26 popr r12 r15
27 popr r1 r15
28 add r13 r13 r12 # res = res + res2
29 jumpr r14 # return res
"""

# Change doDebug to false to turn off debugs
runThis = RecFibSeq
doDebug = True

# Note: main() in the shell to easily reload
def main(runArg=runThis,  debugArg=doDebug):
    Rfrsh(hmmm); hmmm.main(runArg, debugArg)

if __name__ == "__main__" :
    main()
