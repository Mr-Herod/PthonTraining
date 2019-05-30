Description:

"""
That's terrible! Some evil korrigans have abducted you during your sleep and threw you into a maze of thorns in the scrubland D:But have no worry, as long as you're asleep your mind is floating freely in the sky above your body.

Seeing the whole maze from above in your sleep, can you remember the list of movements you'll have to do to get out when you awake?


Input

You are given the whole maze maze as a 2D grid, more specifically in your language:
an array of strings
maze[0][0] is the top left-hand corner
maze[len(maze) - 1][len(maze[0]) - 1] is the bottom right-hand corner
Inside this 2D grid:

' ' is some walkable space  
'#' is a thorn bush (you can't pass through)  
'^', '<', 'v' or '>' is your sleeping body facing respectively the top, left, bottom or right side of the map.


Output

Write the function escape that returns the list/array of moves you need to do relatively to the direction you're facing in order to escape the maze (you won't be able to see the map when you wake up). as an array of the following instructions:  

'F' move one step forward  
'L' turn left  
'R' turn right  
'B' turn back   
Note: 'L','R', and 'B' ONLY perform a rotation and will not move your body



If the maze has no exit, return an empty array.

This is a real maze, there is no "escape" point. Just reach the edge of the map and you're free!
You don't explicitely HAVE to find the shortest possible route, but you're quite likely to timeout if you don't ;P
Aside from having no escape route the mazes will all be valid (they all contain one and only one "body" character and no other characters than the body, "#" and " ". Besides, the map will always be rectangular, you don't have to check that either)


"""

My codes:

def escape(maze):
    verx = len(maze)
    hori = len(maze[0])
    di1 = ["v",">","^","<"]
    for i in maze:
        for j in i:
            if j in di1:
                x,y,dir2 = maze.index(i),i.index(j),j
                break
    
    dic = {(">","<"):"B",("^","v"):"B",("<",">"):"B",("v","^"):"B",
           (">","^"):"L",(">","v"):"R",(">",">"):"",
           ("<","^"):"R",("<","v"):"L",("<","<"):"",
           ("^","^"):"", ("^",">"):"R",("^","<"):"L",
           ("v","v"):"", ("v",">"):"L",("v","<"):"R",}
    
    di  = [(1,0),(0,1),(-1,0),(0,-1)]
    ans = []
    que = [(x,y,dir2,-1)]
    vis = [[False for _ in range(hori)] for _ in range(verx)]
    vis[0][0] = True
    head,tail = 0,1
    flag = 1
    while head != tail and flag:
        pos = que[head]
        for j,i in enumerate(di):
            x = pos[0] + i[0]
            y = pos[1] + i[1]
            if  0 <= x < verx  and 0 <= y < hori and maze[x][y] == ' 'and not vis[x][y]:
                que.append((x,y,di1[j],head))
                vis[x][y] = True
                tail += 1
            if (x == verx-1 or y == hori-1 or x == 0 or y == 0 ) and maze[x][y] == " ":
                flag = 0
                break
        head += 1  
    if flag:
        return []
    p = que[tail-1][3]
    ans.append("F")
    if dic[(que[p][2],que[tail-1][2])] != '':
        ans.append(dic[(que[p][2],que[tail-1][2])])
    while p != 0:
        ans.append("F")
        if dic[(que[que[p][3]][2],que[p][2])] != '':
            ans.append(dic[(que[que[p][3]][2],que[p][2])])
        p = que[p][3]
    return ans[::-1]

Others codes:

from collections import deque
from numpy import cross, dot


MOVES = ((1,0), (-1,0), (0,1), (0,-1))
DIRS  = (  'v',    '^',   '>',    '<')


def escape(maze):
    
    start = x,y = next( (x,y) for x,row in enumerate(maze) for y,c in enumerate(row) if c not in '# ' )
    X, Y, dir   = len(maze), len(maze[0]), MOVES[ DIRS.index(maze[x][y]) ]
    q, seens    = deque([(start, dir)]), {}
    
    if not x or x==X-1 or not y or y==Y-1: return []            # Already at the end, do nothing
    
    noPath = True
    while q:
        (x,y), dir = q.popleft()
        for dx,dy in MOVES:
            xx,yy = pos = (x+dx,y+dy)
            
            if 0 <= xx < X and 0 <= yy < Y and maze[xx][yy]==' ' and pos not in seens:
                q.append( (pos, (dx,dy)) )
                seens[pos] = ((x,y), dir, (dx,dy))              # data: (origin position, direction before origin, direction after origin)
                if not xx or xx==X-1 or not yy or yy==Y-1:      # Escaped!
                    q, noPath = [], False                       # reset the queue to stop it, "from the for loop"
                    break
                    
    if noPath: return []                                        # No path, no chocolate...
    
    path = []
    while pos != start:
        pos, dir, nextDir = seens[pos]
        scal = dot(dir, nextDir)                                # scalar prouct > 0  <=>  go ahead, otherwise, turn back
        prod = cross(dir, nextDir)                              # cross product > 0  <=>  turn left, otherwise, turn right
        if scal: path.append('FB' if scal < 0 else 'F')         # dot != 0 => both directions are colinear
        else:    path.append('FL' if prod > 0 else 'FR')        # orthogonal directions, take a turn
    
    return list(''.join(path)[::-1])

D = {(0,1):{(-1,0):'L', (1,0):'R', (0,-1):'B'}, (1,0):{(0,1):'L', (0,-1):'R', (-1,0):'B'},
     (0,-1):{(1,0):'L', (-1,0):'R', (0,1):'B'}, (-1,0):{(0,-1):'L', (0,1):'R', (1,0):'B'}}
     
def escape(maze):
    P = {(r, c) for r, row in enumerate(maze) for c, v in enumerate(row) if v == ' '}
    
    paths = [[{(r, c) for r, row in enumerate(maze) for c, v in enumerate(row) if v in '<>^v'}.pop()]]
    faces = {'v':(1, 0), '^':(-1,0), '<':(0,-1), '>':(0, 1)}[{c for r in maze for c in r if c in '<>^v'}.pop()]
    
    while paths:
        newp = []
        for path in paths:
            r, c = path[-1]
                
            # Have we escaped?
            if r * c == 0 or r == len(maze) - 1 or c == len(maze[0]) - 1:                
                moves = []
                for p in [(b[0] - a[0], b[1] - a[1]) for a, b in zip(path, path[1:])]:
                    moves += ([D[faces][p]] if faces != p else []) + ['F']
                    faces = p
                return moves
                
            # Are there any more moves to be made on this path?
            for p in {(r+1, c), (r-1, c), (r, c+1), (r, c-1)} & P:
                newp.append(path + [p])
                P.remove(p)
        paths = newp
    return []
