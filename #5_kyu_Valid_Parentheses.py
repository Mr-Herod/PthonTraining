Description:

"""
Write a function called that takes a string of parentheses, and determines if the order of the parentheses is valid. The function should return true if the string is valid, and false if it's invalid.
Examples
"()"              =>  true
")(()))"          =>  false
"("               =>  false
"(())((()())())"  =>  trueConstraints
0 <= input.length <= 100
Along with opening (() and closing ()) parenthesis, input may contain any valid ASCII characters.  Furthermore, the input string may be empty and/or not contain any parentheses at all.  Do not treat other forms of brackets as parentheses (e.g. [], {}, <>).

"""

My codes:

def valid_parentheses(string):
    li = []
    for i in string:
        if i == "(":
            li.append(i)
        elif i == ")":
            try:
                if li.pop() != '(':
                    return False
            except:
                return False
    return len(li) == 0

Others codes:

def valid_parentheses(string):
    cnt = 0
    for char in string:
        if char == '(': cnt += 1
        if char == ')': cnt -= 1
        if cnt < 0: return False
    return True if cnt == 0 else False

def valid_parentheses(string):  
    cnt = 0  
    for char in string:  
        if char == '(': cnt += 1  
        if char == ')': cnt -= 1  
        if cnt < 0: return False  
    return True if cnt == 0 else False 
