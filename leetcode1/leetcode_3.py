def isValid(s):
    s = str(s)
    dict1 = {"(": 1, ")": -1, "[": 2, "]": -2, "{": 3, "}": -3}
    str1 = []
    for i in s:
        if len(str1) == 0:
            str1.append(i)
        elif dict1[i] ^ dict1[str1[-1]] == 0:
            del str1[-1]
        else:
            str1.append(i)
    return len(str1) == 0
s =  "{[]}{}"
print(isValid(s))

