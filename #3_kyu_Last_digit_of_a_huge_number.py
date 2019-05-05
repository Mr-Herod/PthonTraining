Description:

"""
For a given list [x1, x2, x3, ..., xn] compute the last (decimal) digit of 
x1 ^ (x2 ^ (x3 ^ (... ^ xn))). 
E. g.,
last_digit({3, 4, 2}, 3) == 1
int[] array = new int[] {3,4,2};
lastDigit(array) == 1
last_digit({3, 4, 2}) == 1
int[] array = new int[] {3,4,2};
LastDigit(array) == 1
LastDigit([]int{3, 4, 2}) == 1
lastDigit [3, 4, 2] == 1
lastDigit([3, 4, 2]) === 1
last_digit([3, 4, 2]) == 1
because 3 ^ (4 ^ 2) = 3 ^ 16 = 43046721.
Beware: powers grow incredibly fast. For example, 9 ^ (9 ^ 9) has more than 369 millions of digits. lastDigit has to deal with such numbers efficiently.
Corner cases: we assume that 0 ^ 0 = 1 and that lastDigit of an empty list equals to 1.
This kata generalizes Last digit of a large number; you may find useful to solve it beforehand.

"""

My codes:

def last_digit(lst):
    n = 1
    for x in reversed(lst):
        # 如果直接写x ** (n % 4 + 4) ,当n是0时结果就会出错
        n = x ** (n if n < 4 else n % 4 + 4) 
    return n % 10

Others codes:

def last_digit(lst):
    n = 1
    for x in reversed(lst):
        n = x ** (n if n < 4 else n % 4 + 4)
    return n % 10


def last_digit(lst):
    n = 1
    for x in reversed(lst):
        n = x ** (n if n < 4 else n % 4 + 4)
    return n % 10
