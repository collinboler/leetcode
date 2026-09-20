class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        best = 0
        numS = set(nums)

        for num in numS:
            if num - 1 not in numS:
                curr = num
                streak = 1

                while curr + 1 in numS:
                    curr += 1
                    streak += 1
                best = max(best, streak)
        
        return best