Description:

"""
An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.
isIsogram "Dermatoglyphics" == true
isIsogram "moose" == false
isIsogram "aba" == false
isIsogram( "Dermatoglyphics" ) == true
isIsogram( "aba" ) == false
isIsogram( "moOse" ) == false // -- ignore letter case
is_isogram("Dermatoglyphics" ) == true
is_isogram("aba" ) == false
is_isogram("moOse" ) == false # -- ignore letter case
is_isogram("Dermatoglyphics" ) == true
is_isogram("aba" ) == false
is_isogram("moOse" ) == false # -- ignore letter case
is_isogram("Dermatoglyphics" ) == true;
is_isogram("aba" ) == false;
is_isogram("moOse" ) == false; // -- ignore letter case

"""

My codes:

def is_isogram(string):
    new = string.lower()
    list = []
    for i in new:
        if i.isdigit() or i in list:
            return False
        else:
            list.append(i)
    return True

Others codes:

def is_isogram(string):
    return len(string) == len(set(string.lower()))

def is_isogram(string):
    return len(string) == len(set(string.lower())) 
