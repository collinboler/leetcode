class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        solution = 0

        num_set = set(nums)

        for num in num_set:
            # beginning
            if num - 1 not in num_set:
                # intiate run
                curr = num
                streak = 1

                while curr + 1 in num_set:
                    curr += 1
                    streak += 1
                
                solution = max(solution, streak)
        
        return solution


        