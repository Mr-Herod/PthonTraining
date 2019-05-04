Description:

"""
You live in the city of Cartesia where all roads are laid out in a perfect grid.  You arrived ten minutes too early to an appointment, so you decided to take the opportunity to go for a short walk.  The city provides its citizens with a Walk Generating App on their phones -- everytime you press the button it sends you an array of one-letter strings representing directions to walk (eg. ['n', 's', 'w', 'e']).  You always walk only a single block in a direction and you know it takes you one minute to traverse one city block, so create a function that will return true if the walk the app gives you will take you exactly ten minutes (you don't want to be early or late!) and will, of course, return you to your starting point.  Return false otherwise.

Note: you will always receive a valid array containing a random assortment of direction letters ('n', 's', 'e', or 'w' only).  It will never give you an empty array (that's not a walk, that's standing still!).

"""

My codes:

def arrange(strng):
    new = strng.split(" ")
    for i in range(1,len(new)):
        if i % 2:
            if len(new[i-1]) > len(new[i]):
                new[i],new[i-1] = new[i-1],new[i]
            new[i-1] = new[i-1].lower()
        else:
            if len(new[i-1]) < len(new[i]):
                new[i],new[i-1] = new[i-1],new[i]
            new[i-1] = new[i-1].upper()
    if len(new) % 2:
        new[-1] = new[-1].lower()
    else:
        new[-1] = new[-1].upper()
    return " ".join(new)

Others codes:

def isValidWalk(walk):
    return len(walk) == 10 and walk.count('n') == walk.count('s') and walk.count('e') == walk.count('w')

def isValidWalk(walk):
  return len(walk)==10 and walk.count('n')==walk.count('s') and walk.count('e')==walk.count('w')
