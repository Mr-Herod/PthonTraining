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

# Improvements over previous submission:
# - Using regex to pull ints from pile; covers the 'dust123dust456' case (old sol'n would see [123456], new [123, 456])
# - Added early-exit from loop: if a solution that completely fills the basket is found, return it immediately!

import re

def pack_basket(basket, pile):
    dusted = (int(match.group(0)) for match in re.finditer(r'(\d+)', pile))
    lumps_that_fit = (coal for coal in dusted if coal <= basket)
    totals = set((0,))
    template = 'The basket weighs {} kilograms'
    for coal in lumps_that_fit:
        totals |= set(coal + subtotal for subtotal in totals if coal + subtotal <= basket)
        if basket in totals:
            return template.format(basket)
    return template.format(max(totals))
