def string_times(str, n):
    if n <= 0:
        return ""
    return str * n

# print(string_times('Hi', 2))
# print(string_times('Hi', 3))
# print(string_times('Hi', 1))

def front_times(str, n):
    if len(str) < 3:
        return str * n
    return str[:3] * n

# print(front_times('Chocolate', 2))
# print(front_times('Chocolate', 3))
# print(front_times('Abc', 3))

def string_splosion(str):
    s = ""
    for i in range(len(str) + 1):
        s += str[:i]
    return s

print(string_splosion('Code'))
print(string_splosion('abc'))
print(string_splosion('ab'))

def last2(str):
    if len(str) < 2:
        return 0
    last = str[-2:]
    count = 0
    for i in range(len(str) - 2):
        if str[i:i+2] == last:
            count += 1
    return count

    print(last2('hixxhi'))
    print(last2('xaxxaxaxx'))
    print(last2('axxxaaxx'))