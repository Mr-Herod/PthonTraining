"""
Write a program that will calculate the number of trailing zeros in a factorial of a given number.

N! = 1 * 2 * 3 * ... * N

Be careful 1000! has 2568 digits...

For more info, see: http://mathworld.wolfram.com/Factorial.html

Examples
zeros(6) = 1
# 6! = 1 * 2 * 3 * 4 * 5 * 6 = 720 --> 1 trailing zero

zeros(12) = 2
# 12! = 479001600 --> 2 trailing zeros
Hint: You're not meant to calculate the factorial. Find another way to find the number of zeros.
"""

#My codes:

def zeros(n):
    if n < 5:
        return 0    
    else:
        return (int(n/5)+zeros(int(n/5)))

#Others codes:

def zeros(n):
  x = n/5
  return x+zeros(x) if x else 0

def zeros(n):
    return n/5 + zeros(n/5) if n >= 5 else 0

def zeros(n):
    return 0 if n < 5 else n/5 + zeros(n/5)