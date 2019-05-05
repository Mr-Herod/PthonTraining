Description:

"""
John and his wife Ann have decided to go to Codewars. 
On first day Ann will do one kata and John - he wants to know how it is working - 0 kata.
Let us call a(n) the number of katas done by Ann at day n. We have a(0) = 1 and in the same manner j(0) = 0 (or a(1) = 1 and j(1) = 0 for languages that have arrays with indices beginning at 1).
They have chosen the following rules:

On day n the number of katas done by Ann should be n minus the number of katas done by John at day t, t being equal to the number of katas done
by Ann herself at day n - 1.

On day n the number of katas done by John should be n minus the number of katas done by Ann at day t, t being equal to the number of katas done
by John himself at day n - 1.


Whoops! I think they need to lay out a little clearer exactly what there're getting themselves into!
Could you write:

1) two functions ann and john (parameter n) giving the list of the numbers of katas Ann and John should take on the first n days (see first examples below)? 
2) The total number of katas taken by ann function sum_ann(n) and john function sum_john(n) - on the first n days? 

The functions in 1) are not tested in Fortran and not tested in Shell.
Examples:
john(11) -->  [0, 0, 1, 2, 2, 3, 4, 4, 5, 6, 6]
ann(6) -->  [1, 1, 2, 2, 3, 3]

sum_john(75) -->  1720
sum_ann(150) -->  6930Shell Note:
sumJohnAndAnn has two parameters:
first one : n (number of days, $1)
second one : which($2) ->

1 for getting John's sum

2 for getting Ann's sum.


See "Sample Tests".
Note:
Keep an eye on performance.

"""

My codes:

li_john = [0, 0, 1, 2, 2, 3, 4, 4, 5, 6, 6, 7, 7, 8]
li_ann =  [1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6, 7, 8, 8]

for i in range(14,1000000):
    li_ann.append(i - li_john[li_ann[i-1]])
    li_john.append(i - li_ann[li_john[i-1]])
    
def john(n):
    return li_john[:n]
def ann(n):
    return li_ann[:n]
    
def sum_john(n):
    return sum(li_john[:n])
    
def sum_ann(n):
    return sum(li_ann[:n])

Others codes:

def j_n(n):
    j = [0]
    a = [1]
    for i in range(1, n):
        j.append((i - a[j[i-1]]))
        a.append((i-j[a[i-1]]))
    return j, a


def john(n):
    return j_n(n)[0]
    
def ann(n):
    return j_n(n)[1]
    
        
def sum_john(n):
    return sum(john(n))
    
def sum_ann(n):
   return sum(ann(n))

from functools import lru_cache

@lru_cache(maxsize = None)
def john_value(n):
    if n == 0:
        return 0
    return n - ann_value(john_value(n - 1))
    
@lru_cache(maxsize = None)
def ann_value(n):
    if n == 0:
        return 1
    return n - john_value(ann_value(n - 1))

def ann(n):
    return [ann_value(x) for x in range(n)]

def john(n):
    return [john_value(x) for x in range(n)]

def sum_john(n):
    return sum(john(n))
    
def sum_ann(n):
    return sum(ann(n))
