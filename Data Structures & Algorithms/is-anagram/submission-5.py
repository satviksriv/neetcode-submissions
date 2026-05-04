from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return Counter(s) == Counter(t)
        
        # if len(s) != len(t):
        #     return False
        
        # countS, countT = {}, {}

        # for i in range(len(s)):
        #     countS[s[i]] = 1 + countS.get(s[i], 0)
        #     countT[t[i]] = 1 + countT.get(t[i], 0)

        # for c in countS:
        #     if countS[c] != countT.get(c, 0):
        #         return False
        
        # return True

        if len(s) != len(t):
            return False
        
        countS = defaultdict(int)
        countT = defaultdict(int)

        for char in s:
            countS[char] += 1
        
        for char in t:
            countT[char] += 1
        
        for char in countS:
            if countS[char] != countT[char]:
                return False
        
        return True