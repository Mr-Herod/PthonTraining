Description:

"""
Simple, remove the spaces from the string, then return the resultant string.

"""

My codes:

def no_space(x):
    return "".join(x.split())

Others codes:

def no_space(x):
    return x.replace(' ' ,'')

def no_space(x):
    return x.replace(" ", "")
