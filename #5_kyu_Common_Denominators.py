Description:

"""
Common denominators
 You will have a list of rationals in the form 
 { {numer_1, denom_1} , ... {numer_n, denom_n} }  or
 [ [numer_1, denom_1] , ... [numer_n, denom_n] ]  or
 [ (numer_1, denom_1) , ... (numer_n, denom_n) ]  where all numbers are positive ints.
 You have to produce a result in the form 
 (N_1, D) ... (N_n, D)  or
 [ [N_1, D] ... [N_n, D] ] or
 [ (N_1', D) , ... (N_n, D) ] or
{{N_1, D} ... {N_n, D}} depending on the language (See Example tests)
 in which D is as small as possible
 and 
 N_1/D == numer_1/denom_1 ... N_n/D == numer_n,/denom_n.Example: 
convertFracs [(1, 2), (1, 3), (1, 4)] `shouldBe` [(6, 12), (4, 12), (3, 12)]Note:
Due to the fact that first translations were written long ago - more than 4 years - these translations have only irreducible fractions. Newer translations have some reducible fractions. To be on the safe side it is better to do a bit more work by simplifying fractions even if they don't have to be.
Note for Bash:
input is a string,  e.g "2,4,2,6,2,8"
output is  then         "6 12 4 12 3 12"

"""

My codes:

def convertFracts(lst):
    if not lst:
        return []
    greater = lcm([x[1] for x in lst])
    return [[int(greater/x[1])*x[0],greater] for x in lst]

def lcm(lst):
    while len(lst) > 1:
        n,m = max(lst[-1],lst[-2]),min(lst[-1],lst[-2])
        while n%m:
            m,n = n%m,m
        lst[-2] = int(lst[-1]*lst[-2]/m)
        print(lst[-2])
        lst.pop(-1)
    return lst[0]

Others codes:

import math
import functools

def convertFracts(lst):
    lcm = lambda a, b : abs(a*b) // math.gcd(a, b)
    tmp_list = list(map(lambda x : x[1] ,list(lst)))
    lcm_num = functools.reduce(lcm,tmp_list)
    return list(map(lambda x : [x[0] * lcm_num // x[1], lcm_num] , list(lst)))
    

    

from fractions import gcd
from functools import reduce

def lcmm(*numbers): 
    def lcm(a, b):
        return (a * b) // gcd(a, b)
    return reduce(lcm, numbers)
    
def convertFracts(lst):
    denums = tuple(i[1] for i in lst)
    lc = lcmm(*denums)   
    return [[i[0]*(lc//i[1]), lc] for i in lst]
