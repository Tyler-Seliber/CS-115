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
00 setn r15 43
01 read r1
02 calln r14 5
03 write r13
04 halt
05 jnezn r1 8
06 setn r13 0
07 jumpr r14
08 addn r1 -1
09 jnezn r1 12
10 setn r13 1
11 jumpr r14
12 addn r1 1
13 pushr r1 r15
14 pushr r14 r15
15 addn r1 -1
16 calln r14 5
17 popr r14 r15
18 popr r1 r15
19 add r13 r13 r1
20 jumpr r14
21 nop
22 nop
23 nop
24 nop
25 nop
26 nop
27 nop
28 nop
29 nop
30 nop
31 nop
32 nop
33 nop
34 nop
35 nop
36 nop
37 nop
38 nop
39 nop
40 nop
41 nop
42 nop
"""

# Change doDebug to false to turn off debugs
runThis = RecFibSeq
doDebug = False

# Note: main() in the shell to easily reload
def main(runArg=runThis,  debugArg=doDebug):
    Rfrsh(hmmm); hmmm.main(runArg, debugArg)

if __name__ == "__main__" :
    main()
