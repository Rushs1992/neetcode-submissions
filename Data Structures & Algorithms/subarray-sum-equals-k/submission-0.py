class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = currSum = 0
        preSum = {0:1}

        for n in nums:
            currSum += n
            diff = currSum - k
            res += preSum.get(diff,0)
            preSum[currSum] = 1 + preSum.get(currSum, 0)
        
        return res