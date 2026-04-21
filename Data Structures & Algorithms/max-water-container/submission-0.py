class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r,maxWater = 0, len(heights) - 1, 0

        while l < r:
            a,b = r - l, min(heights[l], heights[r])
            maxWater = max(maxWater, a * b)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return maxWater