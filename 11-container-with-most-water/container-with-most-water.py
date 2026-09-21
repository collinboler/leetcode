class Solution(object):
    def area(self, left, right, height):
        return min(height[left], height[right]) * (right - left)
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        # # brute force:
        # best = 0
        # for i, line1 in enumerate(height):
        #     for j, line2 in enumerate(height):
        #         if i == j:
        #             continue
        #         area = min(height[i], height[j]) * abs(i - j)
        #         best = max(area, best)
        
        # return best
        left, right = 0, len(height) - 1
        best = 0
        while left < right:
            # calc area
            area = self.area(left, right, height)
            best = max(best, area)

            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
            
        return best




