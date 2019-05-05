Description:
"""
Some numbers have funny properties. For example:

89 --> 81 + 92 = 89 * 1

695 --> 62 + 93 + 5?= 1390 = 695 * 2

46288 --> 43 + 6?+ 2? + 8? + 8? = 2360688 = 46288 * 51

Given a positive integer n written as abcd... (a, b, c, d... being digits) and a positive integer p

we want to find a positive integer k, if it exists, such as the sum of the digits of n taken to the successive powers of p is equal to k * n.
In other words:

Is there an integer k such as : (a ^ p + b ^ (p+1) + c ^(p+2) + d ^ (p+3) + ...) = n * k

If it is the case we will return k, if not return -1.

Note: n and p will always be given as strictly positive integers.

dig_pow(89, 1) should return 1 since 81 + 92 = 89 = 89 * 1
dig_pow(92, 1) should return -1 since there is no k such as 91 + 22 equals 92 * k
dig_pow(695, 2) should return 2 since 62 + 93 + 5?= 1390 = 695 * 2
dig_pow(46288, 3) should return 51 since 43 + 6?+ 2? + 8? + 8? = 2360688 = 46288 * 51
"""

My codes:

def dig_pow(n, p):
    # your code
    sum = 0
    for i in str(n):
        sum += int(i)**p
        p += 1
    tmp = 1
    while True:
        if tmp*n == sum:
            return tmp
        elif tmp*n > sum:
            return -1
        else:
            tmp += 1
    return -1

Others codes:

def dig_pow(n, p):
  s = 0
  for i,c in enumerate(str(n)):
     s += pow(int(c),p+i)
  return s/n if s%n==0 else -1

def dig_pow(n, p):
    k, fail = divmod(sum(int(d)**(p + i) for i, d in enumerate(str(n))), n)
    return -1 if fail else k
