Description:

"""
Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.
Examples
pigIt('Pig latin is cool'); // igPay atinlay siay oolcay
pigIt('Hello world !');     // elloHay orldway !
pigIt(@"Pig latin is cool"); // => @"igPay atinlay siay oolcay"
pigIt(@"Hello world !");     // => @"elloHay orldway !"
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !
Kata.PigIt("Pig latin is cool"); // igPay atinlay siay oolcay
Kata.PigIt("Hello world !");     // elloHay orldway !
pig_it("Pig latin is cool");   // igPay atinlay siay oolcay
pig_it("Hello world !");       // elloHay orldway
PigLatin.pigIt('Pig latin is cool'); // igPay atinlay siay oolcay
PigLatin.pigIt('Hello world !');     // elloHay orldway !
(piglatin/pig-it "Pig latin is cool") ; "igPay atinlay siay oolcay"
(piglatin/pig-it "Hello world !")     ; "elloHay orldway !"

"""

My codes:

def pig_it(text):
    new = text.split()
    for i in range(len(new)):
        if new[i][0].isalpha():
            new[i] = new[i][1:] + new[i][0] + "ay" + " "
            print(new[i])
    if len(new[-1]) > 1:
        new[-1] = new[-1][:-1]
    return "".join(new)

Others codes:

def pig_it(text):
    lst = text.split()
    return ' '.join( [word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in lst])
    

def pig_it(text):
    lst = text.split()
    return ' '.join( [word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in lst])
