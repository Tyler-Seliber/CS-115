# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Name    : Tyler Seliber
# Pledge  : I pledge my honor that I have abided by the Stevens Honor System.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import random

def shuffledNumbers(n):
    if n <= 0:
        return []
    
    out = list(range(1, n + 1))
    print(out)

    for i in range(n-1, 1, -1):
        j = random.randint(0, i)
        if j < i:
            temp = out[j]
            out[j] = out[i]
            out[i] = temp
    return out

# print(shuffledNumbers(7))