Description:

"""
The Ackermann function is a famous function that played a big role in computability theory as the first exemple of a total computable function that is not primitive recursive.
Since then the function has been a bit simplified but is still of good use. Due to its definition in terms of extremely deep recursion it can be used as a benchmark of a compiler's ability to optimize recursion. 
The goal of this kata is to code a function wich will be given two input, m and n, and will return the Ackermann number A(m,n) defined by:
A(m,n) = n+1                          if m=0  
A(m,n) = A(m-1,1)                     if m>0 , n=0
A(m,n) = A(m-1,A(m,n-1))              if m,n > 0m,n should be non-negative integers, the function should return null (Javascript), None (Python), or nil (Ruby) for other type, non-integer and negative numbers. In C, input is restricted to integer type.

"""

My codes:

def Ackermann(m,n):
  if m == 0:
    return (n+1)
  elif (m > 0) and (n == 0):
    return Ackermann(m-1,1)
  else:
    return Ackermann(m-1,Ackermann(m,n-1))

Others codes:

from numbers import Number
def Ackermann(m,n):
    if isinstance(n, Number) and isinstance(m, Number):
        if m >= 0 and n >= 0:
            return Ackermann_Aux(m,n)
        
    return None

    
def Ackermann_Aux(m,n):
    
    if m == 0:
        return n + 1
    
    if m > 0:
        if n == 0:
            return Ackermann_Aux(m - 1, 1)
        
        if n > 0:
            return Ackermann_Aux(m - 1 , Ackermann_Aux(m, n - 1))
    

def val(v):
  return isinstance(v, int) and v >= 0

def Ackermann(m, n):
  if not val(m) or not val(n): return None
  if m == 0: return n + 1
  elif m > 0 and n == 0: return Ackermann(m - 1, 1)
  return Ackermann(m - 1, Ackermann(m, n - 1))
