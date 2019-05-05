Description:

"""
Given an array, find the int that appears an odd number of times.
There will always be only one integer that appears an odd number of times.

"""

My codes:

def find_it(seq):
    new = list(set(seq))
    for i in new:
        if seq.count(i)%2 == 1:
            return i
    return None


Others codes:

def find_it(seq):
    for i in seq:
        if seq.count(i)%2!=0:
            return i

def find_it(seq):
    for i in seq:
        if seq.count(i) % 2 != 0:
            return i

