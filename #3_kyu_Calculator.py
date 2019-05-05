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

class Calculator(object):
    def evaluate(self, string):
        if not string:
            return None
        new = string.split()
        num = [float(new[0])]
        lens = len(new)
        x = 1
        while x < lens:
            if new[x] == "*":
                num[-1] = num[-1]*float(new[x+1])
            elif new[x]  == "/":
                num[-1] = num[-1]/float(new[x+1])
            elif new[x]  == "-":
                num.append(-float(new[x+1]))
            elif new[x]  == "+":
                num.append(float(new[x+1]))
            x += 2
        ans = sum(num)
        if ans == int(ans):
            return int(ans)
        else:
            return ans

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
