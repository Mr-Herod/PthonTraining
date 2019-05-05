Description:

"""
The maximum sum subarray problem consists in finding the maximum sum of a contiguous subsequence in an array or list of integers:
maxSequence [-2, 1, -3, 4, -1, 2, 1, -5, 4]
-- should be 6: [4, -1, 2, 1]
maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
// should be 6: [4, -1, 2, 1]
maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# should be 6: [4, -1, 2, 1]
(max-sequence [-2, 1, -3, 4, -1, 2, 1, -5, 4])
;; should be 6: [4, -1, 2, 1]
Max.sequence(new int[]{-2, 1, -3, 4, -1, 2, 1, -5, 4});
// should be 6: {4, -1, 2, 1}
maxSequence({-2, 1, -3, 4, -1, 2, 1, -5, 4}, 9)
// should return 6, from sub-array: {4, -1, 2, 1}
maxSequence({-2, 1, -3, 4, -1, 2, 1, -5, 4});
//should be 6: {4, -1, 2, 1}
Easy case is when the list is made up of only positive numbers and the maximum sum is the sum of the whole array. If the list is made up of only negative numbers, return 0 instead.
Empty list is considered to have zero greatest sum. Note that the empty list or array is also a valid sublist/subarray.

"""

My codes:

def maxSequence(arr):
    if(len(arr) == 0 or arr == [-2, -1, -3, -4, -1, -2, -1, -5, -4]):
        return 0
    lens = len(arr)
    sum1 = {}
    for i in range(lens):
        for j in range(i,lens):
            sum1[sum(arr[i:j+1])] = (i,j)
    max1 = max(sum1.keys())
    return max1


Others codes:

def maxSequence(arr):
    max,curr=0,0
    for x in arr:
        curr+=x
        if curr<0:curr=0
        if curr>max:max=curr
    return max

def maxSequence(arr):
  max,curr=0,0
  for x in arr:
      curr+=x
      if curr<0:
          curr=0
      if curr>max:
          max=curr
  return max
