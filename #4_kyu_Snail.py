Description:

"""
Snail Sort
Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.
array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
snail(array) #=> [1,2,3,6,9,8,7,4,5]For better understanding, please follow the numbers of the next array consecutively:
array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
snail(array) #=> [1,2,3,4,5,6,7,8,9]This image will illustrate things more clearly:

NOTE: The idea is not sort the elements from the lowest value to the highest; the idea is to traverse the 2-d array in a clockwise snailshell pattern.
NOTE 2: The 0x0 (empty matrix) is represented as [[]]

"""

My codes:

def snail(array):
    if len(array) == 1:
        return array[0]
    print(array)
    left,right,top,bottom = -1,len(array[0])-1,0,len(array)-1
    x,y,t_r,t_u = 0,1,1,0
    ans = []
    ans.append(array[0][0])
    while left != right or bottom != top :
        ans.append(array[x][y])
        if y == right and x == top:
            t_u = 1
            t_r = 0
            left += 1
        elif y == right and x == bottom:
            t_u = 0
            t_r = -1
            top += 1
        elif y == left and x == bottom:
            t_u = -1
            t_r = 0
            right -= 1
        elif y == left and x == top:
            t_u = 0
            t_r = 1
            bottom -= 1
        x += t_u
        y += t_r
    return ans

Others codes:

def snail(array):
    return list(array[0]) + snail(zip(*array[1:])[::-1]) if array else []

def snail(array):
    return list(array[0]) + snail(zip(*array[1:])[::-1]) if array else []
        
