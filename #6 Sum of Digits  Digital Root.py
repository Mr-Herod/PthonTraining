"""

"""

#My codes:

def digital_root(n):
    sum = 0
    while n != 0:
        sum += n%10
        n = int(n/10)
        if n == 0 and sum < 10:
            return sum
        elif n == 0:
            n = sum
            sum = 0
    return sum

#Others codes:


