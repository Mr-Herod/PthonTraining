Description:

"""
Suzuki is preparing for a walk over fire ceremony high up in the mountains and the monks need coal for the fire. He must pack a basket of coal to the optimal level for each trip up the mountain. He must fit as much as possible into his basket. He can either take a piece of coal or leave it so he must chose which pieces will be optimal for the trip based on the weight in order to maximize the basket capacity.
10 ¡Ü basket ¡Ü 200
1 ¡Ü pile ¡Ü 100
You will be given a data structure similar to the one below:
pile = 'dust 1 dust 4 dust 8 dust 100 dust'

basket = 43

Return the weight of the coal:

'The basket weighs 13 kilograms'

basket = 50

pile = 'dust83dust 45 25 22 46'

Returns:

'The basket weighs 47 kilograms'
Rake out the dust setting the pieces represented as integers for their weight aside. Take as much coal as possible filling the basket as close to its capacity as possible.
The size of the basket will change with each test as Suzuki exchanges it for an empty one on each trip up the mountain.
Return the weight of the coal as a string:
'The basket weighs 13 kilograms'
If there are no pieces of coal that will fit in the basket the solution returns:
'The basket weighs 0 kilograms'
Please also try the other Kata in this series..

Help Suzuki count his vegetables...
Help Suzuki purchase his Tofu!
Help Suzuki rake his garden!
Suzuki needs help lining up his students!
How many stairs will Suzuki climb in 20 years?


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

def pack_basket(basket, pile):
    charges = {0}
    for c in list(map(int, pile.replace('dust', '').split())):
        charges |= {c + d for d in charges if c + d <= basket}
    return 'The basket weighs %d kilograms' % max(charges)

from itertools import combinations
def pack_basket(basket,pile):
    rocks = sorted([int(x) for x in pile.replace('dust', ' ').replace('  ', ' ').split() if int(x) <= basket], reverse=True)
    rocks = sorted([int(x) for x in pile.replace('dust', ' ').replace('  ', ' ').split() if int(x) <= basket], reverse=True)
    print(rocks)
    if sum(rocks) <= basket: return "The basket weighs {0} kilograms".format(sum(rocks))
    if max(rocks) == basket: return "The basket weighs {0} kilograms".format(basket)
    maxcombo = 0
    for i in range(len(rocks) + 1):
        for combo in combinations(rocks, i):
            tst = sum(combo)
            if tst == basket: return "The basket weighs {0} kilograms".format(basket)
            if tst > maxcombo and tst <= basket: maxcombo = tst
    return "The basket weighs {0} kilograms".format(maxcombo)
