Description:

"""
This time we want to write calculations using functions and get the results. Let's have a look at some examples:
JavaScript:
seven(times(five())); // must return 35
four(plus(nine())); // must return 13
eight(minus(three())); // must return 5
six(dividedBy(two())); // must return 3
Ruby:
seven(times(five)) # must return 35
four(plus(nine)) # must return 13
eight(minus(three)) # must return 5
six(divided_by(two)) # must return 3
Requirements:

There must be a function for each number from 0 ("zero") to 9 ("nine")
There must be a function for each of the following mathematical operations: plus, minus, times, dividedBy (divided_by in Ruby)
Each calculation consist of exactly one operation and two numbers
The most outer function represents the left operand, the most inner function represents the right operand
Divison should be integer division, e.g eight(dividedBy(three()))/eight(divided_by(three)) should return 2, not 2.666666...


"""

My codes:

def zero(x = " + 0"):  return int(eval("0" + x))
def one(x = " + 0"):   return int(eval("1" + x))
def two(x = " + 0"):   return int(eval("2" + x))
def three(x = " + 0"): return int(eval("3" + x))
def four(x = " + 0"):  return int(eval("4" + x))
def five(x = " + 0"):  return int(eval("5" + x))
def six(x = " + 0"):   return int(eval("6" + x))
def seven(x = " + 0"): return int(eval("7" + x))
def eight(x = " + 0"): return int(eval("8" + x))
def nine(x = " + 0"):  return int(eval("9" + x))

def plus(x): return "+" + str(x)
def minus(x): return "-" + str(x)
def times(x): return "*" + str(x)
def divided_by(x): return "/" + str(x)

Others codes:

def zero(f = None): return 0 if not f else f(0)
def one(f = None): return 1 if not f else f(1)
def two(f = None): return 2 if not f else f(2)
def three(f = None): return 3 if not f else f(3)
def four(f = None): return 4 if not f else f(4)
def five(f = None): return 5 if not f else f(5)
def six(f = None): return 6 if not f else f(6)
def seven(f = None): return 7 if not f else f(7)
def eight(f = None): return 8 if not f else f(8)
def nine(f = None): return 9 if not f else f(9)

def plus(y): return lambda x: x+y
def minus(y): return lambda x: x-y
def times(y): return lambda  x: x*y
def divided_by(y): return lambda  x: x/y


id_ = lambda x: x
number = lambda x: lambda f=id_: f(x)
zero, one, two, three, four, five, six, seven, eight, nine = map(number, range(10))
plus = lambda x: lambda y: y + x
minus = lambda x: lambda y: y - x
times = lambda x: lambda y: y * x
divided_by = lambda x: lambda y: y / x
