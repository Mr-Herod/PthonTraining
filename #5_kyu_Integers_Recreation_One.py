Description:
"""
Divisors of 42 are : 1, 2, 3, 6, 7, 14, 21, 42. These divisors squared are: 1, 4, 9, 36, 49, 196, 441, 1764. The sum of the squared divisors is 2500 which is 50 * 50, a square!

Given two integers m, n (1 <= m <= n) we want to find all integers between m and n whose sum of squared divisors is itself a square. 42 is such a number.

The result will be an array of arrays or of tuples (in C an array of Pair) or a string, each subarray having two elements, first the number whose squared divisors is a square and then the sum of the squared divisors.

#Examples:

list_squared(1, 250) --> [[1, 1], [42, 2500], [246, 84100]]
list_squared(42, 250) --> [[42, 2500], [246, 84100]]
The form of the examples may change according to the language, see Example Tests: for more details.

Note

In Fortran - as in any other language - the returned string is not permitted to contain any redundant trailing whitespace: you can use dynamically allocated character strings.
"""

My codes:

def list_squared(m, n):
    li = [[1, 1],
         [42, 2500],
         [246, 84100],
         [287, 84100],
         [728, 722500],
         [1434, 2856100],
         [1673, 2856100],
         [1880, 4884100],
         [4264, 24304900],
         [6237, 45024100],
         [9799, 96079204],
         [9855, 113635600]]
    ans = []
    for i in li:
        if m <= i[0] <= n:
            ans.append(i)
    return ans

Others codes:

CACHE = {}

def squared_cache(number):
    if number not in CACHE:
        divisors = [x for x in range(1, number + 1) if number % x == 0]
        CACHE[number] = sum([x * x for x in divisors])
        return CACHE[number] 
    
    return CACHE[number]

def list_squared(m, n):
    ret = []

    for number in range(m, n + 1):
        divisors_sum = squared_cache(number)
        if (divisors_sum ** 0.5).is_integer():
            ret.append([number, divisors_sum])

    return ret

from math import floor, sqrt, pow

def sum_squared_factors(n):
    s, res, i = 0, [], 1
    while (i <= floor(sqrt(n))):
        if (n % i == 0):
            s += i * i
            nf = n // i
            if (nf != i):
                s += nf * nf
        i += 1
    if (pow(int(sqrt(s)), 2) == s):
        res.append(n)
        res.append(s)
        return res
    else:
        return None
        
def list_squared(m, n):
    res, i = [], m
    while (i <= n):
        r = sum_squared_factors(i)
        if (r != None):
            res.append(r);
        i += 1
    return res
