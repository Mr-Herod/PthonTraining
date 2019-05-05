Description:

"""
Given two numbers: 'left' and 'right' (1 <= 'left' <= 'right' <= 200000000000000)
return sum of all '1' occurencies in binary representations of numbers between 'left' and 'right' (including both)
Example:
countOnes 4 7 should return 8, because:
4(dec) = 100(bin), which adds 1 to the result.
5(dec) = 101(bin), which adds 2 to the result.
6(dec) = 110(bin), which adds 2 to the result.
7(dec) = 111(bin), which adds 3 to the result.
So finally result equals 8.WARNING: Segment may contain billion elements, to pass this kata, your solution cannot iterate through all numbers in the segment!

"""

My codes:

def countOnes(left, right): 
    return count(right) - count(left-1)
def count(n):
    s = 0
    while n:
        p = n.bit_length()-1 
        p2 = 1<<p
        n -=  p2
        s += p*(p2>>1)+1 + n
        print (p,s,n)
    return s

Others codes:

import math

def count(n):
    if n is 0: return 0
    x = int(math.log(n, 2))
    return x * 2 ** (x - 1) + n - 2 ** x + 1 + count(n - 2 ** x)

def countOnes(left, right):
    return count(right) - count(left - 1)

sumOnes = lambda n: (lambda msb: n and -~n + ~-msb * 2 ** msb + sumOnes(n - 2 ** -~msb))(n.bit_length() - 2)
countOnes = lambda a, b: sumOnes(b) - sumOnes(a-1)
