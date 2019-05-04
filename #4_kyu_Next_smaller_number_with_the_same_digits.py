Description:

"""
Write a function that takes a positive integer and returns the next smaller positive integer containing the same digits.
For example:
nextSmaller(21) == 12
nextSmaller(531) == 513
nextSmaller(2071) == 2017
nextSmaller(21) == 12
nextSmaller(531) == 513
nextSmaller(2071) == 2017
nextSmaller(21) == 12
nextSmaller(531) == 513
nextSmaller(2071) == 2017
next_smaller(21) == 12
next_smaller(531) == 513
next_smaller(2071) == 2017
next_smaller(21) == 12
next_smaller(531) == 513
next_smaller(2071) == 2017
Return -1 (for Haskell: return Nothing), when there is no smaller number that contains the same digits. Also return -1 when the next smaller number with the same digits would require the leading digit to be zero.
nextSmaller(9) == -1
nextSmaller(111) == -1
nextSmaller(135) == -1
nextSmaller(1027) == -1 // 0721 is out since we don't write numbers with leading zeros
nextSmaller(9) == -1
nextSmaller(111) == -1
nextSmaller(135) == -1
nextSmaller(1027) == -1 // 0721 is out since we don't write numbers with leading zeros
nextSmaller(9) == Nothing
nextSmaller(135) == Nothing
nextSmaller(1027) == Nothing -- 0721 is out since we don't write numbers with leading zeros
next_smaller(9) == -1
next_smaller(135) == -1
next_smaller(1027) == -1  # 0721 is out since we don't write numbers with leading zeros
next_smaller(9) == -1
next_smaller(135) == -1
next_smaller(1027) == -1  # 0721 is out since we don't write numbers with leading zeros

some tests will include very large numbers.
test data only employs positive integers.

The function you write for this challenge is the inverse of this kata: "Next bigger number with the same digits."
"""

My codes:

def isValidWalk(walk):
    if (len(walk) != 10):
        return False
    if(walk.count("n") == walk.count("s") and walk.count("e") == walk.count("w")):
        return True
    return False

Others codes:

def next_smaller(n):
    s = list(str(n))
    i = j = len(s) - 1
    while i > 0 and s[i - 1] <= s[i]: i -= 1
    if i <= 0: return -1
    while s[j] >= s[i - 1]: j -= 1
    s[i - 1], s[j] = s[j], s[i - 1]
    s[i:] = reversed(s[i:])
    if s[0] == '0': return -1
    return int(''.join(s))

def next_smaller(n):
   s = list(str(n))
   i = j = len(s) - 1
   while i > 0 and s[i - 1] <= s[i]: i -= 1
   if i <= 0: return -1
   while s[j] >= s[i - 1]: j -= 1
   s[i - 1], s[j] = s[j], s[i - 1]
   s[i:] = reversed(s[i:])
   if s[0] == '0': return -1
   return int(''.join(s))
