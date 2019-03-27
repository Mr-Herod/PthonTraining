"""
Description:
Bob is preparing to pass IQ test. The most frequent task in this test is to find out which one of the given numbers differs from the others. Bob observed that one number usually differs from the others in evenness. Help Bob ¡ª to check his answers, he needs a program that among the given numbers finds one that is different in evenness, and return a position of this number.

! Keep in mind that your task is to help Bob solve a real IQ test, which means indexes of the elements start from 1 (not 0)

##Examples :

iq_test("2 4 7 8 10") => 3 // Third number is odd, while the rest of the numbers are even

iq_test("1 2 1 1") => 2 // Second number is even, while the rest of the numbers are odd
"""

#My codes:

def iq_test(numbers):
    li = numbers.split(" ")
    for i in range(0,len(li)):
          li[i] = int(li[i])%2
    return li.index((li.count(1) == 1))+1

#Others codes:

def iq_test(numbers):
    e = [int(i) % 2 == 0 for i in numbers.split()]
    return e.index(True) + 1 if e.count(True) == 1 else e.index(False) + 1

def iq_test(numbers):
  a=list(map(lambda x : int(x)%2,numbers.split(' ')))
  return 1+(a.index(0) if (a.count(0)) == 1 else a.index(1))

