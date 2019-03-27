"""
Description:
Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

move_zeros([false,1,0,1,2,0,1,3,"a"]) # returns[false,1,1,2,1,3,"a",0,0]
"""

#My codes:



#Others codes:

def move_zeros(arr):
    l = [i for i in arr if isinstance(i, bool) or i!=0]
    return l+[0]*(len(arr)-len(l))

def move_zeros(array):
    return sorted(array, key=lambda x: x==0 and type(x) is not bool)

def move_zeros(array):
    return sorted(array, key=lambda x: x == 0 and x is not False)

def move_zeros(array):
     return [a for a in array if isinstance(a, bool) or a != 0] + [a for a in array if not isinstance(a, bool) and a == 0]