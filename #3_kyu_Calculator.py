Description:

"""
Create a simple calculator that given a string of operators (+ - * and /) and numbers separated by spaces returns the value of that expression
Example:
Calculator().evaluate("2 / 2 + 3 * 4 - 6") # => 7
Calculator.new.evaluate("2 / 2 + 3 * 4 - 6") # => 7
Calculator.evaluate("2 / 2 + 3 * 4 - 6") // => 7
Calculator.evaluate "2 / 2 + 3 * 4 - 6" // => 7.0
Remember about the order of operations! Multiplications and divisions have a higher priority and should be performed left-to-right. Additions and subtractions have a lower priority and should also be performed left-to-right.
"""

My codes:

def format_duration(second):
    if second == 0:
        return "now"
    seconds = second%60
    minutes= int((second%3600)/60)
    hours  = int((second%86400)/3600)
    days   = int((second%31536000)/86400)
    years  = int(second/31536000)
    tmp = sum([1 for x in [seconds,minutes,hours,days,years] if x > 0])
    ans = [x for x in [["years",years],["days",days],["hours",hours],["minutes",minutes],["seconds",seconds]] if x[1]>0]
    if tmp == 1:
        if ans[0][1] == 1:
            return str(ans[0][1])+ " " + ans[0][0][:-1]
        else:
            return str(ans[0][1])+ " " + ans[0][0]
    elif tmp == 2:
        new = ""
        if ans[0][1] == 1:
            new += str(ans[0][1])+ " " + ans[0][0][:-1] + " and "
        else:
            new += str(ans[0][1])+ " " + ans[0][0] + " and "
        if ans[1][1] == 1:
            new += str(ans[1][1])+ " " + ans[1][0][:-1]
        else:
            new += str(ans[1][1])+ " " + ans[1][0]
        return new
    elif tmp >= 3:
        new = ""
        for x in ans[:-2]:
            if x[1] == 1:
                new += str(x[1])+ " " + x[0][:-1] + ", "
            else:
                new += str(x[1])+ " " + x[0] + ", "
        if ans[-2][1] == 1:
            new += str(ans[-2][1])+ " " + ans[-2][0][:-1] + " and "
        else:
            new += str(ans[-2][1])+ " " + ans[-2][0] + " and "
        if ans[-1][1] == 1:
            new += str(ans[-1][1])+ " " + ans[-1][0][:-1]
        else:
            new += str(ans[-1][1])+ " " + ans[-1][0]
        return new

Others codes:

from operator import add, sub, mul, div

FIRST = {'*' : mul, '/': div}
SECOND = {'+': add, '-': sub}

class Calculator(object):
    def evaluate(self, string):
        tokens = [float(t) if t.isdigit() or '.' in t else t for t in string.split()]
        while True:
            for (i, token) in enumerate(tokens):
                op = FIRST.get(token)
                if op:
                    tokens[i - 1 : i + 2] = [op(tokens[i - 1], tokens[i + 1])]
                    break
            else:
                ret = tokens[0]
                for i in xrange(1, len(tokens), 2):
                    ret = SECOND[tokens[i]](ret, tokens[i + 1])
                return ret if ret != 7.986000000000001 else 7.986 # Bug in test



from operator import add, sub, mul, div

FIRST = {'*' : mul, '/': div}
SECOND = {'+': add, '-': sub}

class Calculator(object):
    def evaluate(self, string):
        tokens = [float(t) if t.isdigit() or '.' in t else t for t in string.split()]
        while True:
            for (i, token) in enumerate(tokens):
                op = FIRST.get(token)
                if op:
                    tokens[i - 1 : i + 2] = [op(tokens[i - 1], tokens[i + 1])]
                    break
            else:
                ret = tokens[0]
                for i in xrange(1, len(tokens), 2):
                    ret = SECOND[tokens[i]](ret, tokens[i + 1])
                return ret if ret != 7.986000000000001 else 7.986 # Bug in test
