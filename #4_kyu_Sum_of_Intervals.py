Description:

"""
Write a function called sumIntervals/sum_intervals() that accepts an array of intervals, and returns the sum of all the interval lengths. Overlapping intervals should only be counted once.
Intervals
Intervals are represented by a pair of integers in the form of an array. The first value of the interval will always be less than the second value. Interval example: [1, 5] is an interval from 1 to 5. The length of this interval is 4.
Overlapping Intervals
List containing overlapping intervals:
[
   [1,4],
   [7, 10],
   [3, 5]
]The sum of the lengths of these intervals is 7. Since [1, 4] and [3, 5] overlap, we can treat the interval as [1, 5], which has a length of 4.
Examples:
sumIntervals( [
   [1,2],
   [6, 10],
   [11, 15]
] ); // => 9

sumIntervals( [
   [1,4],
   [7, 10],
   [3, 5]
] ); // => 7

sumIntervals( [
   [1,5],
   [10, 20],
   [1, 6],
   [16, 19],
   [5, 11]
] ); // => 19
// null argument
Interval.sumIntervals(null);  // => 0

// empty intervals
Interval.sumIntervals(new int[][]{});  // => 0
Interval.sumIntervals(new int[][]{2,2}, {5,5});  // => 0

// disjoined intervals
Interval.sumIntervals(new int[][]{
  {1,2},{3,5}
});  // => (2-1) + (5-3) = 3

// overlapping intervals
Interval.sumIntervals(new int[][]{
  {1,4},{3,6},{2,8}
});  // [1,8] => 7
sum_intervals( {
   {1,2},
   {6, 10},
   {11, 15}
} ); // => 9

sum_intervals( {
   {1,4},
   {7, 10},
   {3, 5}
} ); // => 7

sum_intervals( {
   {1,5},
   {10, 20},
   {1, 6},
   {16, 19},
   {5, 11}
} ); // => 19

"""

My codes:

def sum_of_intervals(intervals):
    lenth,i = 0,0
    lens = len(intervals)
    intervals.sort(key = lambda x:x[0])
    while i < lens:
        j = i + 1
        while j < lens and intervals[i][1] > intervals[j][1]:
            intervals.pop(j)
            lens -= 1
        i = j
    lens,i,j = len(intervals),0,0
    while i < lens:
        j = i + 1
        while j < lens and intervals[j][0] < intervals[j-1][1]:
            j += 1
        if j != i+1:
            lenth += intervals[j-1][1] - intervals[i][0]
        else:
            lenth += intervals[i][1] - intervals[i][0]
        if i == j-1:
            i += 1
        else:
            i = j
    return lenth

Others codes:

def sum_of_intervals(intervals):
    s, top = 0, float("-inf")
    for a,b in sorted(intervals):
        if top < a: top    = a
        if top < b: s, top = s+b-top, b
    return s

def sum_of_intervals(intervals):
    return len(set([n for (a, b) in intervals for n in [i for i in range(a, b)]]))
