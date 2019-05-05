Description:

"""
Your task is to sort a given string. Each word in the string will contain a single number. This number is the position the word should have in the result.
Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).
If the input string is empty, return an empty string.
The words in the input String will only contain valid consecutive numbers.
Examples
"is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
"4of Fo1r pe6ople g3ood th5e the2"  -->  "Fo1r the2 g3ood 4of th5e pe6ople"
""  -->  ""
"""

My codes:

def order(sentence):
    if not sentence:
        return ""
    new = [int(i) for i in sentence if i.isdigit()]
    word = sentence.split()
    ans = word.copy()
    for c,i in enumerate(new):
        ans[i-1] = word[c]
    return " ".join(ans)

Others codes:

def order(sentence):
    return " ".join(sorted(sentence.split(), key=lambda x: int(filter(str.isdigit, x))))

def order(sentence):
  return ' '.join(sorted(sentence.split(), key=lambda x:  int(filter(str.isdigit, x))))
