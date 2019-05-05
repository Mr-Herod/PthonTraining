Description:

"""
Kate constantly finds herself in some kind of a maze. Help her to find a way out!.
For a given maze and Kate's position find if there is a way out. Your function should return True or False.
Each maze is defined as a list of strings, where each char stays for a single maze "cell". ' ' (space) can be stepped on, '#' means wall and 'k' stays for Kate's starting position. Note that the maze may not always be square or even rectangular.
Kate can move left, up, right or down only.
There should be only one Kate in a maze. In any other case you have to throw an exception.
Example input
['# ##',
 '# k#',
 '####']Example output
True
Example input
['####'.
 '# k#',
 '####']Example output
False

"""

My codes:

def has_exit(maze):
    W = len(maze[0])                                                    # W = width of the maze
    S = W * len(maze)                                                   # S = total cells in the maze
    frontier, unseen = set(), set()                                     # Declaring sets that we'll use for BFS
    for position, content in enumerate("".join(maze)):                  # Use 1D representation for unique address of each cell
        (frontier.add, unseen.add, id)["k #".index(content)](position)  # Populate our sets: put Kate into frontier, passages into unseen
    assert len(frontier) == 1                                           # Check for one and only one Kate
    while frontier:                                                     # Do we still have any options to move further?
        position = frontier.pop()                                       # Take out one of the options
        if min(position, S - position) < W or -~position % W < 2:       # Is it on the edge?
            return True                                                 # If so, we found an exit! Hurray!
        for way in (position - W,                                       # Look up
                    position + W,                                       # Look down
                    position - 1,                                       # Look left
                    position + 1):                                      # Look right
            if way in unseen:                                           # If there is no wall, there is a way
                frontier.add (way)                                      # Let's add this to our options
                unseen.remove(way)                                      # We've seen it already
    return False    

Others codes:

MOVES = {(0,1), (0,-1), (1,0), (-1,0)}

def has_exit(maze):
    posSet = {(x,y) for x in range(len(maze)) for y in range(len(maze[x])) if maze[x][y] == 'k'}
    if len(posSet) != 1:
        raise ValueError("There shouldn't be more than one kate")
    
    seen = set(posSet)
    while posSet:
        x,y = posSet.pop()
        if any(not (0 <= x+dx < len(maze) and 0 <= y+dy < len(maze[x+dx])) for dx,dy in MOVES):
            return True
        neighbors = {(x+dx, y+dy) for dx,dy in MOVES if 0 <= x+dx < len(maze) and 0 <= y+dy < len(maze[x+dx])
                                                        and maze[x+dx][y+dy] == ' '
                                                        and (x+dx, y+dy) not in seen}
        posSet |= neighbors
        seen   |= neighbors
    return False

def has_exit(maze):
    vector, w = list("".join(maze)), len(maze[0])                # "vector" is 1D representation of the maze; "w" is the width of a maze row
    assert vector.count("k") == 1                                # checking if there is one and only one Kate in the maze
    while "k" in vector:                                         # cycle that pushes Kate clones into previously unvisited adjacent cells
        for p, cell in enumerate(vector):                        # sweeping the maze...
            if cell == "k":                                      # ...for Kate clones
                if min(p, len(vector) - p) < w or -~p % w < 2:   # Kate clone at edge?
                    return True                                  # exit found!
                for direction in (-w, 1, w, -1):                 # otherwise look at adjacent cells
                    if  vector[p + direction] == " ":            # to see if clone can pass through them
                        vector[p + direction]  = "k"             # clone Kate where there is a passage
                vector[p] = "+"                                  # mark cell as visited
    return False                                                 # There is no exit :(

