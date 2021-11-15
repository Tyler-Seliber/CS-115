def fibonacci(n):
    if n == 0:
        res = 0
        return res
    n = n - 1
    if n == 0:
        res = 1
        return res
    
    res = fibonacci(n)
    n = n - 1
    res2 = fibonacci(n)
    res = res + res2
    return res

print(fibonacci(9))