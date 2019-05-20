Description:

"""
Simple, given a string of words, return the length of the shortest word(s).
String will never be empty and you do not need to account for different data types.

"""

My codes:

def find_short(s):
    return min( [len(i) for i in s.split()] )

Others codes:

def find_short(s):
    return min(len(x) for x in s.split())

def find_short(s):
    return min(len(x) for x in s.split(" "))
    
