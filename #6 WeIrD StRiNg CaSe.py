"""
Description:
Write a function toWeirdCase (weirdcase in Ruby) that accepts a string, and returns the same string with all even indexed characters in each word upper cased, and all odd indexed characters in each word lower cased. The indexing just explained is zero based, so the zero-ith index is even, therefore that character should be upper cased.

The passed in string will only consist of alphabetical characters and spaces(' '). Spaces will only be present if there are multiple words. Words will be separated by a single space(' ').

Examples:
to_weird_case('String'); # => returns 'StRiNg'
to_weird_case('Weird string case') # => returns 'WeIrD StRiNg CaSe'
"""

#My codes:

def to_weird_case(string):
    tmp = -1
    s = ""
    for i in range(len(string)):
        if string[i] == " ":
            tmp = i%2
            s += " "
        elif i%2 == (tmp+1)%2:
            s += string[i].upper()
        else:
            s += string[i].lower()
    return s

#Others codes:

def to_weird_case_word(string):
    return "".join(c.upper() if i%2 == 0 else c for i, c in enumerate(string.lower()))
    
def to_weird_case(string):
    return " ".join(to_weird_case_word(str) for str in string.split())

def to_weird_case(string):
    recase = lambda s: "".join([c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(s)])
    return " ".join([recase(word) for word in string.split(" ")])

def to_weird_case(string):
    return ' '.join([''.join([y.lower() if i%2 else y.upper() for i, y in enumerate(x)]) for x in string.split()])

def to_weird_case(string):
    return ' '.join(map(lambda w: ''.join(l.lower() if i%2 else l.upper() for i,l in enumerate(w)), string.split()))