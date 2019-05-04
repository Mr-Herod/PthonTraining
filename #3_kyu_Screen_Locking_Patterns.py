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

li_john = [0, 0, 1, 2, 2, 3, 4, 4, 5, 6, 6, 7, 7, 8]
li_ann =  [1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6, 7, 8, 8]

for i in range(14,1000000):
    li_ann.append(i - li_john[li_ann[i-1]])
    li_john.append(i - li_ann[li_john[i-1]])
    
def john(n):
    return li_john[:n]
def ann(n):
    return li_ann[:n]
    
def sum_john(n):
    return sum(li_john[:n])
    
def sum_ann(n):
    return sum(li_ann[:n])

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
