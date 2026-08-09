class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        smallest_seen = float('inf')
        for price in prices:
            max_profit = max(max_profit, price - smallest_seen)
            smallest_seen = min(smallest_seen, price)
        return max_profit