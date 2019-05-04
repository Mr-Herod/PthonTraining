Description:

"""
You are given an array strarr of strings and an integer k. Your task is to return the first longest string
consisting of k consecutive strings taken in the array.
Example:
longest_consec(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2) --> "abigailtheta"
n being the length of the string array, if n = 0 or k > n or k <= 0 return "".
Note
consecutive strings : follow one after another without an interruption
"""

My codes:

class Dictionary:
    def __init__(self,words):
        self.words = words
        self.get_words()
    def find_most_similar(self,term):
        print(term)
        most = 1000
        lens = len(term)
        ans = self.words[0]
        for i in self.words:
            for k in range(len(i)):
                si = 0
                for j in range(lens):
                    try:
                        if term[j] != i[k+j]:
                            si += 1
                    except:
                        si += k
                        break
                si += abs(len(i) - lens)
                #print(si,i)
                if si < most:
                    most = si
                    ans = i
        return ans
    def get_words(self):
        print(self.words)

Others codes:

def longest_consec(strarr, k):
    result = ""
    
    if k > 0 and len(strarr) >= k:
        for index in range(len(strarr) - k + 1):
            s = ''.join(strarr[index:index+k])
            if len(s) > len(result):
                result = s
            
    return result

def longest_consec(strarr, k):
   
    result = ""
    
    if k > 0 and len(strarr) >= k:
        for index in range(len(strarr) - k + 1):
            s = ''.join(strarr[index:index+k])
            if len(s) > len(result):
                result = s 
            
    return result
