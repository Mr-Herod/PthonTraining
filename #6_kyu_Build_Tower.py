Description:

"""
Build Tower
Build Tower by the following given argument:
number of floors (integer and always greater than 0).
Tower block is represented as *

Python: return a list;
JavaScript: returns an Array;
C#: returns a string[];
PHP: returns an array;
C++: returns a vector<string>;
Haskell: returns a [String];
Ruby: returns an Array;

Have fun!

for example, a tower of 3 floors looks like below
[
  '  *  ', 
  ' *** ', 
  '*****'
]and a tower of 6 floors looks like below
[
  '     *     ', 
  '    ***    ', 
  '   *****   ', 
  '  *******  ', 
  ' ********* ', 
  '***********'
]
Go challenge Build Tower Advanced once you have finished this :)

"""

My codes:

def tower_builder(n_floors):
    return  [" "*(n_floors-1-i) + (2*i+1)*"*" + " "*(n_floors-1-i) for  i in range(n_floors)]


Others codes:

def tower_builder(n):
    return [("*" * (i*2-1)).center(n*2-1) for i in range(1, n+1)]


def tower_builder(n):
    return [('*' * (i*2-1)).center(n*2-1) for i in range(1, n+1)]
