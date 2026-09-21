class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        min_price = float("inf")
        best = 0

        for i, num in enumerate(prices):
            if num < min_price:
                min_price = num
            elif num - min_price > best:
                best = num - min_price
        
        return best
