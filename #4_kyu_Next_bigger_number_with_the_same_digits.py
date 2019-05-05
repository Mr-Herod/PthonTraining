Description:

"""
You have to create a function that takes a positive integer number and returns the next bigger number formed by the same digits:
12 ==> 21
513 ==> 531
2017 ==> 2071
If no bigger number can be composed using those digits, return -1:
9 ==> -1
111 ==> -1
531 ==> -1

"""

My codes:

def next_bigger(n):
    l1 = list(str(n))
    l1.reverse()
    flag = False
    for i in range(len(l1)):
        for j in range(i):
            if l1[j] > l1[i]:
                flag = True
                break
        if flag:
            break
    if flag:
        l1[i],l1[j] = l1[j],l1[i]
        l1[:i] = sorted(l1[:i],reverse = True)
    if "".join(reversed(l1)) != str(n):
        return int("".join(reversed(l1)))
    else:
        return -1

Others codes:

import itertools
def next_bigger(n):
    s = list(str(n))
    for i in range(len(s)-2,-1,-1):
        if s[i] < s[i+1]:
            t = s[i:]
            m = min(filter(lambda x: x>t[0], t))
            t.remove(m)
            t.sort()
            s[i:] = [m] + t
            return int("".join(s))
    return -1


import itertools
def next_bigger(n):
    s = list(str(n))
    for i in range(len(s)-2,-1,-1):
        if s[i] < s[i+1]:
            t = s[i:]
            m = min(filter(lambda x: x>t[0], t))
            t.remove(m)
            t.sort()
            s[i:] = [m] + t
            return int("".join(s))
    return -1
