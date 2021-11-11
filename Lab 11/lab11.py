# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Name    : Tyler Seliber
# Pledge  : I pledge my honor that I have abided by the Stevens Honor System.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Wubba = """

00 setn r15 16
01 read r1
02 calln r14 5
03 write r13
04 halt
05 jnezn r1 8
06 setn r13 1
07 jumpr r14
08 pushr r1 r15
09 pushr r14 r15
10 addn r1 -1
11 calln r14 5
12 popr r14 r15
13 popr r1 r15
14 mul r13 r13 r1
15 jumpr r14

"""

# 1. How low could you start the stack?

# 2. How deep does the stack get?

# 3. What are the possible values of r14?

# ~~~~~ Running ~~~~~~
import hmmm
import importlib

runThis = Wubba  # Change to the function you want to run
doDebug = True # Change to turn debug mode on/off

# call main() from the command line to run the program again
def main(runArg = runThis, debugArg = doDebug):
    importlib.reload(hmmm)
    hmmm.main(runArg, debugArg)

if __name__ == "__main__" : 
    main()


