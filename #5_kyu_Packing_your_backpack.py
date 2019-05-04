Description:

"""
You're about to go on a trip around the world! On this trip you're bringing your trusted backpack, that anything fits into. The bad news is that the airline has informed you, that your luggage cannot exceed a certain amount of weight.
To make sure you're bringing your most valuable items on this journey you've decided to give all your items a score that represents how valuable this item is to you. It's your job to pack you bag so that you get the most value out of the items that you decide to bring.
Your input will consist of two arrays, one for the scores and one for the weights. You input will always be valid lists of equal length, so you don't have to worry about verifying your input.
You'll also be given a maximum weight. This is the weight that your backpack cannot exceed.
For instance, given these inputs:
scores = [15, 10, 9, 5]
weights = [1, 5, 3, 4]
capacity = 8The maximum score will be 29. This number comes from bringing items 1, 3 and 4.
Note: Your solution will have to be efficient as the running time of your algorithm will be put to a test.
"""

My codes:

def pack_basket(basket,pile):
    while "dust" in pile:
        pile = pile.replace("dust"," ")
    new = pile.strip().split(" ")
    while '' in new:
        new.remove("")
    print(new)
    pack = [0 for i in range(1000)]
    for i in range(len(new)):
        for j in range(basket,int(new[i])-1,-1):
            pack[j] = max(pack[j-int(new[i])]+int(new[i]),pack[j])
    return 'The basket weighs {} kilograms'.format(pack[basket])

Others codes:

def pack_bagpack(S,W,C) :
    M = [0] * (1 + C)
    for F,V in enumerate(S) :
        M = [max(U,M[T - W[F]] + V if W[F] <= T else 0) for T,U in enumerate(M)]
    return M[-1]

def pack_bagpack(scores,weights,capacity):
    sols=[[0 for j in range(capacity+1)] for i in range(len(scores)+1)]
    scores.insert(0, 0)
    weights.insert(0, 0)
    for y,iy in enumerate(sols[1:],1):
        for x,ix in enumerate(iy[1:],1):
            if weights[y]<=x:
                sols[y][x]=max(scores[y]+sols[y-1][x-weights[y]],sols[y-1][x])
            else:
                sols[y][x]=sols[y-1][x]
    return sols[-1][-1]
