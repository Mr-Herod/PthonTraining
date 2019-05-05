Description:

"""
The prime numbers are not regularly spaced. For example from 2 to 3 the gap is 1.
From 3 to 5 the gap is 2. From 7 to 11 it is 4.
Between 2 and 50 we have the following pairs of 2-gaps primes:
3-5, 5-7, 11-13, 17-19, 29-31, 41-43
A prime gap of length n is a run of n-1 consecutive composite numbers between two successive primes (see: http://mathworld.wolfram.com/PrimeGaps.html).
We will write a function gap with parameters:
g (integer >= 2) which indicates the gap we are looking for
m (integer > 2) which gives the start of the search (m inclusive)
n (integer >= m) which gives the end of the search (n inclusive)
In the example above gap(2, 3, 50) will return [3, 5] or (3, 5) or {3, 5} which is the first pair between 3 and 50 with a 2-gap.
So this function should return the first pair of two prime numbers spaced with a gap of g
between the limits m, n if these numbers exist otherwise nil or null or None or Nothing (depending on the language). 
In C++ return in such a case {0, 0}. In F# return [||]. In Kotlin return []
#Examples:
gap(2, 5, 7) --> [5, 7] or (5, 7) or {5, 7}
gap(2, 5, 5) --> nil. In C++ {0, 0}. In F# [||]. In Kotlin return[]`
gap(4, 130, 200) --> [163, 167] or (163, 167) or {163, 167}
([193, 197] is also such a 4-gap primes between 130 and 200 but it's not the first pair)
gap(6,100,110) --> nil or {0, 0} : between 100 and 110 we have 101, 103, 107, 109 but 101-107is not a
6-gap because there is 103in between and 103-109is not a 6-gap because there is 107in between.
Note for Go
For Go: nil slice is expected when there are no gap between m and n.
Example: gap(11,30000,100000) --> nil
#Ref
https://en.wikipedia.org/wiki/Prime_gap

"""

My codes:

import math
def gap(g, m, n):
    
    if m%2 == 0:
        m += 1
    for i in range(m,n+1,2):
        if isprime(i) and isprime(i+g) and not sum([isprime(x) for x in range(i+1,i+g)]):
            return [i,i+g]
    return None

def isprime(number):
    if number > 1:
        if number == 2:
            return 1
        if number % 2 == 0:
            return 0
        for current in range(3, int(math.sqrt(number) + 1), 2):
            if number % current == 0: 
                return 0
        return 1
    return 0

Others codes:

def gap(g, m, n):
    previous_prime = n
    for i in range(m, n + 1):
        if is_prime(i):
            if i - previous_prime == g: 
                return [previous_prime, i]
            previous_prime = i
    return None
            
    
def is_prime(n):
    for i in range(2, int(n**.5 + 1)):
        if n % i == 0:
            return False
    return True

def gap(g, m, n):
    
    def _try_composite(a, d, n, s):
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2**i * d, n) == n-1:
                return False
        return True # n  is definitely composite

    # Miller-Rabin primarility test (rosettacode implementation)
    def is_prime(n, _precision_for_huge_n=16):
        if n in _known_primes or n in (0, 1):
            return True
        if any((n % p) == 0 for p in _known_primes):
            return False
        d, s = n - 1, 0
        while not d % 2:
            d, s = d >> 1, s + 1
        # Returns exact according to http://primes.utm.edu/prove/prove2_3.html
        if n < 1373653: 
            return not any(_try_composite(a, d, n, s) for a in (2, 3))
        if n < 25326001: 
            return not any(_try_composite(a, d, n, s) for a in (2, 3, 5))
        if n < 118670087467: 
            if n == 3215031751: 
                return False
            return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7))
        if n < 2152302898747: 
            return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11))
        if n < 3474749660383: 
            return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13))
        if n < 341550071728321: 
            return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13, 17))
        # otherwise
        return not any(_try_composite(a, d, n, s) 
                       for a in _known_primes[:_precision_for_huge_n])

    _known_primes = [2, 3]
    _known_primes += [x for x in range(5, 1000, 2) if is_prime(x)]

    # Check initial pre-conditions
    assert((g, m) >= (2, 2))
    assert(n >= m)    
    
    a, b = None, None
    
    for current in xrange(m + 1 if m % 2 == 0 else m, n, 2):
        if is_prime(current):
            a, b = b, current
            if a is not None and b is not None and (b - a) == g:
                    return [a, b]
        
    return None
