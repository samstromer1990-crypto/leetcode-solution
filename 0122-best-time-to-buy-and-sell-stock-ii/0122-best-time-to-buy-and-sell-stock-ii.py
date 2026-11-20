class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        
        i = 0
        profit = 0
        while (i < len(prices)-1):
            if prices[i] < prices[i+1]:
                profit += prices[i+1] - prices[i]
                i+=1
            else:
                i+=1
        return profit
        