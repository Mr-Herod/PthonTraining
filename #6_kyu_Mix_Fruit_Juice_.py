Description:

"""
Story
Jumbo Juice makes a fresh juice out of fruits of your choice.Jumbo Juice charges $5 for regular fruits and $7 for special ones. Regular fruits are Banana, Orange, Apple, Lemon and Grapes. Special ones are Avocado, Strawberry and Mango. Others fruits that are not listed are also available upon request. Those extra special fruits cost $9 per each. There is no limit on how many fruits she/he picks.The price of a cup of juice is the mean of price of chosen fruits. In case of decimal number (ex. $5.99), output should be the nearest integer (use the standard rounding function of your language of choice). 

Input
The function will receive an array of strings, each with the name of a fruit. The recognition of names should be case insensitive. There is no case of an enmpty array input.  


Example
['Mango', 'Banana', 'Avocado'] //the price of this juice bottle is (7+5+7)/3 = $6($6.333333...)
"""

My codes:

def mix_fruit(arr):
    li1 = ["banana", "orange","apple", "lemon","grapes"]
    li2 = ["avocado", "strawberry" ,"mango"]
    ans = 0
    for i in arr:
        if i.lower() in li1:
            ans += 5
        elif i.lower() in li2:
            ans += 7
        else:
            ans += 9
    if (ans/len(arr)) > int(ans/len(arr))+0.5:
        return int(ans/len(arr)) + 1
    return int(ans/len(arr))

Others codes:

def mix_fruit(arr):
    regular = ["banana", "orange", "apple", "lemon", "grapes"]
    special = ["avocado", "strawberry", "mango"]
    return round(sum(5 if fruit.lower() in regular else (7 if fruit.lower() in special else 9) for fruit in arr)/len(arr))


from collections import defaultdict
from statistics import mean

prices = defaultdict(lambda: 9)
prices.update(dict.fromkeys(['banana', 'orange', 'apple', 'lemon', 'grapes'], 5))
prices.update(dict.fromkeys(['avocado', 'strawberry', 'mango'], 7))

def mix_fruit(arr):
    return round(mean(prices[fruit.lower()] for fruit in arr))
