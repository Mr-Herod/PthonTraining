Description:

"""
Sum Array
Write a method sum (sum_array in python, SumArray in C#) that takes an array of numbers and returns the sum of the numbers. These may be integers or decimals for Ruby and any instance of Num for Haskell. The numbers can also be negative. If the array does not contain any numbers then you should return 0.
Examples
numbers = [1, 5.2, 4, 0, -1]
puts sum(numbers)
9.2
IO.inspect SumNumbers.sum([1, 5.2, 4, 0, -1])
9.2
sum([1, 5.2, 4, 0, -1]); // => 9.2
print $ sum [1, 5.2, 4, 0, -1]
> 9.2

print $ sum []
> 0
sum [1, 5.2, 4, 0, -1]
> 9.2

sum []
> 0
(println (sum [1 2 3]))
> 6
(println (sum []))
> 0
print sum_array([1 2 3])
> 6
print sum_array([])
> 0
Kata.SumArray(new int[] {1, 2, 3}) => 6
sum_array(c(1, 5.2, 4, 0, -1))
[1] 9.2
sum_array(c())
[1] 0
Assumptions

You can assume that you are only given numbers.
You cannot assume the size of the array.
You can assume that you do get an array and if the array is empty, return 0.

What We're Testing
We're testing basic loops and math operations. This is for beginners who are just learning loops and math operations.
Disclaimer
This is for beginners so we want to test basic loops and math operations. Advanced users may find this extremely easy and can easily write this in one line.

"""

My codes:

def sum_array(a):
    if a==[]:
        return 0
    else:
        return sum(a)

Others codes:

def sum_array(a):
  return sum(a)

def sum_array(a):
    return sum(a)
