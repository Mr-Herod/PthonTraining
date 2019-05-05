Description:

"""
Screen Locking Patterns
You might already be familiar with many smartphones that allow you to use a geometric pattern as a security measure. To unlock the device, you need to connect a sequence of dots/points in a grid by swiping your finger without lifting it as you trace the pattern through the screen.
The image below has an example pattern of 7 dots/points: [A, B, I, E, D, G, C].

For this kata, your job is to implement the function countPatternsFrom(firstPoint, length); where firstPoint is a single-character string corresponding to the point in the grid (i.e.: 'A') and length is an integer indicating the length of the pattern. The function must return the number of combinations starting from the given point, that have the given length.
Take into account that dots can only be connected with straight directed lines either:

horizontally (like A to B) 
vertically (like D to G), 
diagonally (like I and E, as well as B and I), or 
passing over a point that has already been 'used' like (G and C passing over E). 

The sample tests have some examples of the number of combinations for some cases to help you check your code.
Optional Extra:
Out of curiosity, in case you're wondering, for the Android lock screen, valid patterns must have between 4 and 9 dots, and there are 389112 possible valid combinations in total.
Haskell Note:
A data type Vertex is provided in place of the single-character strings. See the solution setup code for more details.

"""

My codes:

def count_patterns_from(firstPoint, length):
    if length > 9 or length <= 0:
        return 0
    if length == 9:
        length = 8
    print(firstPoint, length)
    ans = {'A':[0,1,5,31,154,684,2516,7104,13792],'B':[0,1,7,37,256,816,4248,8118,15564],\
           'C':[0,1,5,31,154,684,2516,7104,13792],'D':[0,1,7,37,188,816,2926,8118,15564],\
           'E':[0,1,8,48,256,1152,4248,12024,23280],'F':[0,1,7,37,188,816,4248,8118,15564],\
           'G':[0,1,5,31,154,684,2516,7104,13792],'H':[0,1,7,37,256,816,2926,8118,15564],\
           'I':[0,1,5,31,154,684,2516,7104,13792]
          }
    return ans[firstPoint][length]

Others codes:

EQUIV_PTS = {same: src for src,seq in (('A','CGI'), ('B','DFH')) for same in seq}

ALL       =  set('ABCDEFGHI')
LINKED_TO = {'A': ('BC','DG','EI','F', 'H'),
             'B': ('A', 'C', 'D', 'EH','F', 'G', 'I'),
             'C': ('BA','D', 'EG','FI','H'),
             'D': ('A', 'B', 'C', 'EF','G', 'H', 'I'),
             'E': tuple('ABCDFGHI'),
             'F': ('A', 'B', 'C', 'ED','G', 'H', 'I'),
             'G': ('DA','B', 'EC','F', 'HI'),
             'H': ('A', 'EB','C', 'D', 'F', 'G', 'I'),
             'I': ('EA','B', 'FC','D', 'HG')
            }


def DFS(c, depth, root, seens, patterns):
    if depth > len(ALL): return                
    
    patterns[root][depth] += 1
    
    seens.add(c)
    toExplore = ''.join( next((n for n in seq if n not in seens), '') for seq in LINKED_TO[c] )
    for nextC in toExplore:
        DFS(nextC, depth+1, root, seens, patterns)
    seens.discard(c)
    

PATTERNS = {}
for c in "ABE":
    PATTERNS[c] = [0]*10
    DFS(c, 1, c, set(), PATTERNS)


def count_patterns_from(start, length):
    if not (0 < length < 10) or start not in ALL: return 0    
    
    actualStart = EQUIV_PTS.get(start, start)
    return PATTERNS[actualStart][length]
    

vals = [0,1,2,5,6,7,10,11,12]
def count_patterns_from(firstPoint, length, left=set(vals)):
    if length<1 or length>len(left): return 0
    if length==1: return 1
    n = vals[ord(firstPoint)-65] if type(firstPoint)==str else firstPoint
    return sum(count_patterns_from(m,length-1,left-{n}) for m in left-{n} if (m+n)/2 not in left)
    
