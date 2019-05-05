Description:

"""
When you divide the successive powers of 10 by 13 you get the following remainders of the integer divisions:  
1, 10, 9, 12, 3, 4. 
Then the whole pattern repeats.
Hence the following method:
Multiply the right most digit of the number with the left most number 
in the sequence shown above, the second right most digit to the second 
left most digit of the number in the sequence. The cycle goes on and you sum all these products. Repeat this process until the sequence of sums is stationary.
...........................................................................
Example: What is the remainder when 1234567 is divided by 13?
7¡Á1 + 6¡Á10 + 5¡Á9 + 4¡Á12 + 3¡Á3 + 2¡Á4 + 1¡Á1 = 178
We repeat the process with 178:
8x1 + 7x10 + 1x9 = 87
and again with 87:
7x1 + 8x10 = 87
...........................................................................
From now on the sequence is stationary and the remainder of 1234567 by 13 is 
the same as the remainder of 87 by 13: 9
Call thirt the function which processes this sequence of operations on an integer n (>=0). thirt will return the stationary number.
thirt(1234567) calculates 178, then 87, then 87 and returns 87.
thirt(321) calculates 48, 48 and returns 48

"""

My codes:

def thirt(n):
    li = [1, 10, 9, 12, 3, 4]
    new = [int(x) for x in str(n)][::-1]
    s   =  100000
    while s >= 100:
        s = 0
        for i in range(len(new)):
            s += new[i]*li[i%6]
        new = [int(x) for x in str(s)][::-1]
    return s

Others codes:

array = [1, 10, 9, 12, 3, 4]

def thirt(n):
    total = sum([int(c) * array[i % 6] for i, c in enumerate(reversed(str(n)))])
    if n == total:
        return total
    return thirt(total)


array = [1, 10, 9, 12, 3, 4]

def thirt(n):
    total = sum([int(c) * array[i % 6] for i, c in enumerate(reversed(str(n)))])
    if n == total:
        return total
    return thirt(total)
