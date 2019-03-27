"""
Given an array of one's and zero's convert the equivalent binary value to an integer.

Eg: [0, 0, 0, 1] is treated as 0001 which is the binary representation of 1.

Examples:

Testing: [0, 0, 0, 1] ==> 1
Testing: [0, 0, 1, 0] ==> 2
Testing: [0, 1, 0, 1] ==> 5
Testing: [1, 0, 0, 1] ==> 9
Testing: [0, 0, 1, 0] ==> 2
Testing: [0, 1, 1, 0] ==> 6
Testing: [1, 1, 1, 1] ==> 15
Testing: [1, 0, 1, 1] ==> 11
"""

#My codes:
def binary_array_to_number(arr):
  sum = 1
  tmp = 1
  new = arr[::-1]
  for i in new:
      sum += int(i)*tmp
      tmp *= 2
  return sum-1

#Other codes:

def binary_array_to_number(arr):
  return int("".join(map(str, arr)), 2)

def binary_array_to_number(arr):
    return int(''.join(str(a) for a in arr), 2)