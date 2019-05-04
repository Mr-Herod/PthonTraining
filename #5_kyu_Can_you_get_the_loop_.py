Description:

"""
You are given a node that is the beginning of a linked list. This list always contains a tail and a loop.
Your objective is to determine the length of the loop.  
For example in the following picture the tail's size is 3 and the loop size is 11.

# Use the `next' method to get the following node.

node.next
// Use the `getNext' method or 'next' property to get the following node.

node.getNext()
node.next
# Use the `next' attribute to get the following node

node.next
// Use the `getNext()` method to get the following node.

node.getNext()
-- use the `next :: Node a -> Node a` function to get the following node
# Use the `next' method to get the following node.

node.next
Note: do NOT mutate the nodes!

Thanks to shadchnev, I broke all of the methods from the Hash class.


Don't miss dmitry's article in the discussion after you pass the Kata !! 

"""

My codes:

import math
def gap(g, m, n):
    
    if m%2 == 0:
        m += 1
    for i in range(m,n+1,2):
        if isprime(i) and isprime(i+g) and not sum([isprime(x) for x in range(i+1,i+g)]):
            return [i,i+g]
    return None

def isprime(number):
    if number > 1:
        if number == 2:
            return 1
        if number % 2 == 0:
            return 0
        for current in range(3, int(math.sqrt(number) + 1), 2):
            if number % current == 0: 
                return 0
        return 1
    return 0

Others codes:

def loop_size(node):
    turtle, rabbit = node.next, node.next.next
    
    # Find a point in the loop.  Any point will do!
    # Since the rabbit moves faster than the turtle
    # and the kata guarantees a loop, the rabbit will
    # eventually catch up with the turtle.
    while turtle != rabbit:
        turtle = turtle.next
        rabbit = rabbit.next.next
  
    # The turtle and rabbit are now on the same node,
    # but we know that node is in a loop.  So now we
    # keep the turtle motionless and move the rabbit
    # until it finds the turtle again, counting the
    # nodes the rabbit visits in the mean time.
    count = 1
    rabbit = rabbit.next
    while turtle != rabbit:
        count += 1
        rabbit = rabbit.next

    # voila
    return count

def loop_size(node):
    index = {}
    i = 0
    while True:
        if node in index:
            return i - index[node]
        index[node] = i
        node = node.next
        i += 1
