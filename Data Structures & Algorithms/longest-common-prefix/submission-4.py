class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""

        smallest = strs[0]

        for s in strs:
            if len(s) < len(smallest):
                smallest = s
        
        for i in range(len(smallest)):
            for s in strs:
                if s[i] != smallest[i]:
                    return ans
            ans += smallest[i]
        
        return ans