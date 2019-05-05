Description:

"""
I'm sure, you know Google's "Did you mean ...?", when you entered a search term and mistyped a word. In this kata we want to implement something similar.
You'll get an entered term (lowercase string) and an array of known words (also lowercase strings). Your task is to find out, which word from the dictionary is most similar to the entered one. The similarity is described by the minimum number of letters you have to add, remove or replace in order to get from the entered word to one of the dictionary. The lower the number of required changes, the higher the similarity between each two words.
Same words are obviously the most similar ones. A word that needs one letter to be changed is more similar to another word that needs 2 (or more) letters to be changed. E.g. the mistyped term berr is more similar to beer (1 letter to be replaced) than to barrel (3 letters to be changed in total).
Extend the dictionary in a way, that it is able to return you the most similar word from the list of known words.
Code Examples:
fruits = new Dictionary(['cherry', 'pineapple', 'melon', 'strawberry', 'raspberry']);
fruits.findMostSimilar('strawbery'); // must return "strawberry"
fruits.findMostSimilar('berry'); // must return "cherry"

things = new Dictionary(['stars', 'mars', 'wars', 'codec', 'codewars']);
things.findMostSimilar('coddwars'); // must return "codewars"

languages = new Dictionary(['javascript', 'java', 'ruby', 'php', 'python', 'coffeescript']);
languages.findMostSimilar('heaven'); // must return "java"
languages.findMostSimilar('javascript'); // must return "javascript" (same words are obviously the most similar ones)
Dictionary fruits = new Dictionary(new String[]{"cherry", "pineapple", "melon", "strawberry", "raspberry"});

fruits.findMostSimilar("strawbery"); // must return "strawberry"
fruits.findMostSimilar("berry"); // must return "cherry"

Dictionary things = new Dictionary(new String[]{"stars", "mars", "wars", "codec", "codewars"});
things.findMostSimilar("coddwars"); // must return "codewars"

Dictionary languages = new Dictionary(new String[]{"javascript", "java", "ruby", "php", "python", "coffeescript"});
languages.findMostSimilar("heaven"); // must return "java"
languages.findMostSimilar("javascript"); // must return "javascript" (same words are obviously the most similar ones)
var fruits = new Kata(new List<string> { "cherry", "pineapple", "melon", "strawberry", "raspberry" });
fruits.FindMostSimilar("strawbery"); // must return "strawberry"
fruits.FindMostSimilar("berry"); // must return "cherry"

things = new Dictionary(new List<string> { "stars", "mars", "wars", "codec", "codewars" });
things.FindMostSimilar("coddwars"); // must return "codewars"

languages = new Dictionary(new List<string> { "javascript", "java", "ruby", "php", "python", "coffeescript" });
languages.FindMostSimilar("heaven"); // must return "java"
languages.FindMostSimilar("javascript"); // must return "javascript" (same words are obviously the most similar ones)
I know, many of you would disagree that java is more similar to heaven than all the other ones, but in this kata it is ;)
Additional notes:

there is always exactly one possible solution


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

# Hjelmqvist, Sten: Fast, memory efficient Levenshtein algorithm
def LevenshteinDistance(s, t):
    sLen = len(s)
    tLen = len(t)
    
    if (sLen == 0): return tLen
    if (tLen == 0): return sLen
    v0 = range(tLen+1)
    v1 = [0]*(tLen+1)
    for i in range(sLen):
        v1[0] = i + 1
        for j in range(tLen):
            cost = 0 if s[i] == t[j] else 1
            v1[j + 1] = min(v1[j] + 1, v0[j + 1] + 1, v0[j] + cost)
        v0 = list(v1)
    return v1[tLen]

class Dictionary:
    def __init__(self,words):
        self.words=words

    def find_most_similar(self,term):
        dist = {}
        for word in words:
            dist[word] = LevenshteinDistance(word, term)
        return min(dist, key=dist.get)

from itertools import izip, cycle

def cache_it(function):
    cache = {}
    def dec_cache_it(*args):
        entry = cache.get(args)
        if not entry:
            entry = function(*args)
            cache[args] = entry
        return entry
    return dec_cache_it

@cache_it
def dist(lhs, rhs, l=0, r=0):
    if l == len(lhs): return len(rhs) - r
    if r == len(rhs): return len(lhs) - l
    d = bool(lhs[l] != rhs[r])
    return d  + min(dist(lhs, rhs, l + 1, r + 1),
                    dist(lhs, rhs, l + 1, r),
                    dist(lhs, rhs, l, r + 1))

class Dictionary:
    def __init__(self, words):
        self.words = words
        
    def _find_most_similar(self, term):
        for word in words:
            yield dist(word, term), word
        
    def find_most_similar(self, term):
        return min(self._find_most_similar(term), key=lambda e: e[0])[1]
        

