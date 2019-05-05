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

def longest_consec(strarr, k):
    n = len(strarr)
    if n == 0 or k > n or k <= 0:
        return ""
    ans = ""
    for i in range(n):
        s = ""
        try:
            for j in strarr[i:i+k]:
                s += j
            if len(s) > len(ans):
                ans = s
        except:
            break
    return ans

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
