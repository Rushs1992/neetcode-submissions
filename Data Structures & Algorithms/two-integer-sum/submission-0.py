class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        checked = {}
        for i,n in enumerate(nums):
            goal = target - n
            if goal in checked:
                return [checked[goal], i]
            else:
                checked[n] = i