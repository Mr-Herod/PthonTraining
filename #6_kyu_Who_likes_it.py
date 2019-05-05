Description:

"""
You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. We want to create the text that should be displayed next to such an item.
Implement a function likes :: [String] -> String, which must take in input array, containing the names of people who like an item. It must return the display text as shown in the examples:
likes [] // must be "no one likes this"
likes ["Peter"] // must be "Peter likes this"
likes ["Jacob", "Alex"] // must be "Jacob and Alex like this"
likes ["Max", "John", "Mark"] // must be "Max, John and Mark like this"
likes ["Alex", "Jacob", "Mark", "Max"] // must be "Alex, Jacob and 2 others like this"
Kata.Likes(new string[0]) => "no one likes this"
Kata.Likes(new string[] {"Peter"}) => "Peter likes this"
Kata.Likes(new string[] {"Jacob", "Alex"}) => "Jacob and Alex like this"
Kata.Likes(new string[] {"Max", "John", "Mark"}) => "Max, John and Mark like this"
Kata.Likes(new string[] {"Alex", "Jacob", "Mark", "Max"}) => "Alex, Jacob and 2 others like this"
* return must be an allocated string
* do not mutate input

likes({})
    // should return "no one likes this"

likes({"Peter"})
    // should return "Peter likes this"

likes({"Jacob", "Alex"})
    // should return "Jacob and Alex like this"

likes({"Max","John","Mark"})
    // should return "Max, John and Mark like this"

likes({"Alex", "Jacob", "Mark", "Max"})
    // should return "Alex, Jacob and 2 others like this"

likes {} // must be "no one likes this"
likes {"Peter"} // must be "Peter likes this"
likes {"Jacob", "Alex"} // must be "Jacob and Alex like this"
likes {"Max", "John", "Mark"} // must be "Max, John and Mark like this"
likes {"Alex", "Jacob", "Mark", "Max"} // must be "Alex, Jacob and 2 others like this"
likes {} // must be "no one likes this"
likes {"Peter"} // must be "Peter likes this"
likes {"Jacob", "Alex"} // must be "Jacob and Alex like this"
likes {"Max", "John", "Mark"} // must be "Max, John and Mark like this"
likes {"Alex", "Jacob", "Mark", "Max"} // must be "Alex, Jacob and 2 others like this"
For 4 or more names, the number in and 2 others simply increases.

"""

My codes:

def likes(names):
    lens = len(names)
    if lens == 0:
        return "no one likes this"
    if lens == 1:
        return names[0] + " likes this"
    if lens == 2:
        return names[0] + " and " + names[1] + " like this"
    if lens == 3:
        return names[0] + ", " + names[1] + " and " + names[2] + " like this"
    return names[0] + ", " + names[1] + " and "+ str(lens-2) +" others like this"

Others codes:

def likes(names):
    n = len(names)
    return {
        0: 'no one likes this',
        1: '{} likes this', 
        2: '{} and {} like this', 
        3: '{}, {} and {} like this', 
        4: '{}, {} and {others} others like this'
    }[min(4, n)].format(*names[:3], others=n-2)

def likes(names):
     n = len(names) 
     return { 
     0: 'no one likes this',
     1: '{} likes this', 
     2: '{} and {} like this', 
     3: '{}, {} and {} like this', 
     4: '{}, {} and {others} others like this' }[min(4, n)].format(*names[:3], others=n-2)

     
 
