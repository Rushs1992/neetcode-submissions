class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        minBuy = prices[0]

        for stocks in prices:
            maxP = max(maxP, stocks - minBuy)
            minBuy = min(minBuy, stocks)
        return maxP
