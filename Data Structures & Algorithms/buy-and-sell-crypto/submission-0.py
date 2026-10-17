class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m = float('inf')
        profit = 0

        for num in prices:
            if num < m:
                m = num
            elif num - m > profit:
                profit = num - m
            
        return profit
        # [10,1,5,6,7,1] m = 1 profit = 0
