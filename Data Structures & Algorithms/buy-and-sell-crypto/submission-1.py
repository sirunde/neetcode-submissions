class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hold = prices[0]
        sell = 0
        for i in prices:
            if hold > i:
                hold = i

            if i - hold > sell:
                sell = i - hold

        return sell