from collections import deque
class Solution(object):
    def findBuildings(self, heights):
        """
        :type heights: List[int]
        :rtype: List[int]
        """
        solution = deque()
        
        tallest = 0
        i = len(heights) - 1
        while i > -1:
            if heights[i] > tallest:
                tallest = heights[i]
                solution.appendleft(i)
            i -= 1
        
        return list(solution)

        



        