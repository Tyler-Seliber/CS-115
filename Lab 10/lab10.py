# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Name    : Tyler Seliber
# Pledge  : I pledge my honor that I have abided by the Stevens Honor System.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Max:
#  Write a hmmm function that gets two numbers,
#   then prints the larger of the two.
#  Assumptions: Both inputs are any integers
Max = """
00 read r1
01 read r2
02 sub r3 r1 r2
03 jgtzn r3 06
04 write r2
05 jumpn 07
06 write r1
07 halt
"""


# Power:
#  Write a hmmm function that gets two numbers,
#   then prints (No.1 ^ No.2).
#  Assumptions: No.1 is any integer, No.2 >= 0
Power = """
00 read r1
01 read r2
02 setn r3 1
03 setn r4 1
04 jeqzn r2 08
05 mul r3 r3 r1
06 sub r2 r2 r4
07 jumpn 04
08 write r3
09 halt
"""


# Fibonacci
#  Write a hmmm function that gets one number,
#   then prints the No.1st fibonacci number.
#  Assumptions: No.1 >= 0
#  Tests: f(2) = 1
#         f(5) = 5
#         f(9) = 34
Fibonacci = """
00 setn r15 42
01 read r1
02 setn r2 0
03 setn r3 1
04 pushr r2 r15
05 pushr r3 r15
06 calln r14 09
07 write r13
08 halt
09 jnezn r1 13
10 popr r14 r15
11 popr r13 r15
12 jumpr r14
13 addn r1 -1
14 calln r14 09
15 popr r2 r15
16 add r3 r2 r13
17 pushr r2 r15
18 popr r13 r15
19 popr r14 r15
20 jumpr r14
"""


# ~~~~~ Running ~~~~~~
import hmmm
import importlib

runThis = Fibonacci  # Change to the function you want to run
doDebug = True # Change to turn debug mode on/off

# call main() from the command line to run the program again
def main(runArg = runThis, debugArg = doDebug):
    importlib.reload(hmmm)
    hmmm.main(runArg, debugArg)

if __name__ == "__main__" : 
    main()


