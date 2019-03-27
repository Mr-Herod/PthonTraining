"""
Implement a function that adds two numbers together and returns their sum in binary. The conversion can be done before, or after the addition.

The binary number returned should be a string.
"""

#My codes:

def add_binary(a,b):
    li = ""
    sum = a + b
    while sum != 0:
        li += str(sum%2)
        sum /= 2
    return li[::-1]

#Others codes:

def add_binary(a,b):
    return bin(a+b)[2:]

def add_binary(a,b):
    return '{0:b}'.format(a + b)

def add_binary(a, b):
    return format(a + b, 'b')