class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tCount = {}
        reqCount = {}
        have, need = 0 , len(tCount)
        res, resLen = [-1,-1], int(1100)
        l = 0

        for c in t:
            tCount[c] = 1 + tCount.get(c,0)
        need = len(tCount)
            
        for r in range(len(s)):
            c = s[r]
            reqCount[c] = 1 + reqCount.get(c,0)

            if c in tCount and reqCount[c] == tCount[c]:
                have += 1
            
            while have == need:
                if(r-l+1) < resLen:
                    res = [l,r]
                    resLen = r-l+1
                
                reqCount[s[l]] -=1
                if s[l] in tCount and reqCount[s[l]] < tCount[s[l]]:
                    have -=1
                l +=1
        l,r = res
        return s[l:r+1] if resLen != 1100 else ""