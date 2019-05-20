Description:

"""
You have an array of numbers.Your task is to sort ascending odd numbers but even numbers must be on their places.
Zero isn't an odd number and you don't need to move it. If you have an empty array, you need to return it.
Example
sortArray([5, 3, 2, 8, 1, 4]) == [1, 3, 2, 8, 5, 4]
sortArray([5, 3, 2, 8, 1, 4]) == [1, 3, 2, 8, 5, 4]
sort_array([5, 3, 2, 8, 1, 4]) == [1, 3, 2, 8, 5, 4]
sort_array([5, 3, 2, 8, 1, 4]) == [1, 3, 2, 8, 5, 4]
sort_array([5, 3, 2, 8, 1, 4]) == [1, 3, 2, 8, 5, 4]
sortArray [5, 3, 2, 8, 1, 4] == [1, 3, 2, 8, 5, 4]

"""

My codes:

def sort_array(source_array):
    if source_array == []:
        return []
    new = sorted([x for x in source_array if x%2 == 1])
    j = 0
    for i in range(len(source_array)):
        if source_array[i] %2 == 1 :
            source_array[i] = new[j]
            j += 1
    return source_array

Others codes:

def sort_array(arr):
  odds = sorted((x for x in arr if x%2 != 0), reverse=True)
  return [x if x%2==0 else odds.pop() for x in arr]

def sort_array(arr):
    odds = sorted((x for x in arr if x%2 != 0), reverse=True)
    return [x if x%2==0 else odds.pop() for x in arr]
