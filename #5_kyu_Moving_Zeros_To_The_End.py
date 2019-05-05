Description:

"""
Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.
moveZeros([false,1,0,1,2,0,1,3,"a"]) // returns[false,1,1,2,1,3,"a",0,0]
move_zeros([false,1,0,1,2,0,1,3,"a"]) # returns[false,1,1,2,1,3,"a",0,0]
moveZeros [false,1,0,1,2,0,1,3,"a"] # returns[false,1,1,2,1,3,"a",0,0]
Kata.MoveZeroes(new int[] {1, 2, 0, 1, 0, 1, 0, 3, 0, 1}) => new int[] {1, 2, 1, 1, 3, 1, 0, 0, 0, 0}

"""

My codes:

def move_zeros(array):
    count = array.count(0)
    li = []
    lens = len(array)
    i = 0
    while i < lens:
        if array[i] == 0 and (type(array[i]) == type(0) or type(array[i]) == type(0.0)):
            li.append(array[i])
            del array[i]

            lens -= 1
        else:
            i += 1
    array.append(0)
    array[-1:] = li
    return array
            

Others codes:

def move_zeros(arr):
    l = [i for i in arr if isinstance(i, bool) or i!=0]
    return l+[0]*(len(arr)-len(l))

def move_zeros(array):
    return sorted(array, key=lambda x: x == 0 and x is not False)
