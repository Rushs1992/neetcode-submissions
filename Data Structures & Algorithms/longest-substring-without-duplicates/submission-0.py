class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cmap = {}
        l = 0
        result = 0

        for r in range(len(s)):
            if s[r] in cmap:
                l = max(cmap[s[r]]+1, l)
            cmap[s[r]] = r
            result = max(result, r-l +1)
        
        return result

