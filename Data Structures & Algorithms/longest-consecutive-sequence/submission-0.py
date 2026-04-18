class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        for n in nums:
            maxLength = 0
            if (n-1) not in numSet:
                i = n
                while i in numSet:
                    maxLength +=1
                    i += 1
                longest = max(longest,maxLength)
        return longest