"""
Description:
Write Number in Expanded Form
You will be given a number and you will need to return it as a string in Expanded Form. For example:

expanded_form(12) # Should return '10 + 2'
expanded_form(42) # Should return '40 + 2'
expanded_form(70304) # Should return '70000 + 300 + 4'
NOTE: All numbers will be whole numbers greater than 0.

If you liked this kata, check out part 2!!
"""

#My codes:

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

#Others codes:

def expanded_form(num):
    num = list(str(num))
    return ' + '.join(x + '0' * (len(num) - y - 1) for y,x in enumerate(num) if x != '0')

def expanded_form(num):
    num = str(num)
    st = ''
    for j, i in enumerate(num):
        if i != '0':
            st += ' + {}{}'.format(i, (len(num[j+1:])*'0'))
    return st.strip(' +')

def expanded_form(num):
    return " + ".join([str(int(d) * 10**p) for p, d in enumerate(str(num)[::-1]) if d != "0"][::-1])

def expanded_form(num):
    return ' + '.join([x+'0'*i for i,x in enumerate(str(num)[::-1]) if x != '0'][::-1])


