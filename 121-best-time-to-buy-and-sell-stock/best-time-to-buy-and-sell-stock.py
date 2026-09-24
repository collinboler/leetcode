class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # goal: greatest right - left differential
        # find min 
        minPrice = float('inf')
        maxProfit = 0 
        for price in prices:
            if price < minPrice:
                minPrice = price
            if price - minPrice > maxProfit:
                maxProfit = price - minPrice
        
        return maxProfit

        






        