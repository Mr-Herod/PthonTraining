Description:

"""
Write a function which outputs the positions of matching bracket pairs. The output should be a dictionary with keys the positions of the open brackets '(' and values the corresponding positions of the closing brackets ')'.
For example: input = "(first)and(second)" should return {0:6, 10:17}
If brackets cannot be paired or if the order is invalid (e.g. ')(') return False. In this kata we care only about the positions of round brackets '()', other types of brackets should be ignored.

"""

My codes:

def bracket_pairs(string):
    if string.count("(") != string.count(")"):
        return False
    elif string.count(")") == 0:
        return {}
    li1,li2 = [],[]
    for i in range(len(string)):
        if string[i] == "(":
            li1.append(i)
        elif string[i] == ")":
            try:
                li2.append([li1.pop(),i])
            except:
                return False
    li2.sort(key = lambda x:x[0])
    return {x[0]:x[1] for x in li2}

Others codes:

def bracket_pairs(string):
    brackets = {}
    open_brackets = []

    for i, c in enumerate(string):
        if c == '(':
            open_brackets.append(i)
        elif c == ')':
            if not open_brackets:
                return False
            brackets[open_brackets.pop()] = i

    return False if open_brackets else brackets


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

def bracket_pairs(s):
    l = len(s);
    stack = Stack(); i = 0; res = {}; flag = True
    while i < l and flag:
        if s[i] == "(": stack.push(i)
        elif  s[i] == ")":
            if stack.is_empty(): flag = False
            else: 
                a = stack.pop()
                res[a] = i
        i += 1
    if flag and stack.is_empty(): return res
    return False
