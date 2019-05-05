Description:

"""
Write Number in Expanded Form
You will be given a number and you will need to return it as a string in Expanded Form. For example:
expandedForm 12    -- Should return '10 + 2'
expandedForm 42    -- Should return '40 + 2'
expandedForm 70304 -- Should return '70000 + 300 + 4'
expandedForm(12); // Should return '10 + 2'
expandedForm(42); // Should return '40 + 2'
expandedForm(70304); // Should return '70000 + 300 + 4'
expanded_form(12) # Should return '10 + 2'
expanded_form(42) # Should return '40 + 2'
expanded_form(70304) # Should return '70000 + 300 + 4'
expanded_form(12); // Should return "10 + 2"
expanded_form(42); // Should return "40 + 2"
expanded_form(70304); // Should return "70000 + 300 + 4"
expanded_form(12); # Should return '10 + 2'
expanded_form(42); # Should return '40 + 2'
expanded_form(70304); # Should return '70000 + 300 + 4'
expandedForm(12); # Should return '10 + 2'
expandedForm(42); # Should return '40 + 2'
expandedForm(70304); # Should return '70000 + 300 + 4'
Kata.expandedForm(12); # Should return "10 + 2"
Kata.expandedForm(42); # Should return "40 + 2"
Kata.expandedForm(70304); # Should return "70000 + 300 + 4"
Kata.ExpandedForm(12); # Should return "10 + 2"
Kata.ExpandedForm(42); # Should return "40 + 2"
Kata.ExpandedForm(70304); # Should return "70000 + 300 + 4"
expandedForm 12L // Should return "10 + 2"
expandedForm 42L // Should return "40 + 2"
expandedForm 70304L // Should return "70000 + 300 + 4"
NOTE: All numbers will be whole numbers greater than 0.
If you liked this kata, check out part 2!!

"""

My codes:

def expanded_form(num):
    tmp = 1
    li = []
    s = ""
    while num > 0:
        li.append((num%10) * tmp)
        num = int(num/10)
        tmp *= 10
    for i in reversed(li):
        if li.index(i) == len(li) - 1:
            s += str(i)
        elif i != 0:
            s += " + " + str(i)
    return s

Others codes:

def expanded_form(num):
    num = list(str(num))
    return ' + '.join(x + '0' * (len(num) - y - 1) for y,x in enumerate(num) if x != '0')

def expanded_form(n):
    result = []
    for a in range(len(str(n)) - 1, -1, -1):
        current = 10 ** a
        quo, n = divmod(n, current)
        if quo:
            result.append(str(quo * current))
    return ' + '.join(result)
