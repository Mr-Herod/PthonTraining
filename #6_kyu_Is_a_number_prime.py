Description:

"""
Define a function that takes an integer argument and returns logical value true or false depending on if the integer is a prime.
Per Wikipedia, a prime number (or a prime) is a natural number greater than 1 that has no positive divisors other than 1 and itself.
Example
is_prime(1)  /* false */
is_prime(2)  /* true  */
is_prime(-1) /* false */
mov edi, 1
call is_prime    ; EAX <- 0 (false)

mov edi, 2
call is_prime    ; EAX <- 1 (true)

mov edi, -1
call is_prime    ; EAX <- 0 (false)bool isPrime(5) = return true
Assumptions

You can assume you will be given an integer input.
You can not assume that the integer will be only positive. You may be given negative numbers as well (or 0).
There are no fancy optimizations required, but still the most trivial solutions might time out. Try to find a solution which does not loop all the way up to n.


"""

My codes:

def is_prime(num):
    from math import sqrt
    if (num <= 1):
        return False
    for i in range(2,int(sqrt(num))+1):
        if num%i == 0:
            return False
    else:
        return True

Others codes:

def is_prime(num):
    return num > 1 and not any(num % n == 0 for n in range(2,num))

def is_prime(num):
  return num > 1 and not any(num % n == 0 for n in range(2, num))
