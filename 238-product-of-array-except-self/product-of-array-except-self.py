class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        right, left, solution = [0] * len(nums), [0] * len(nums), [0] * len(nums)

        # start with left
        left[0] = 1
        for i in range(1, len(nums)):
            left[i] = left[i - 1] * nums[i - 1]
        # then right
        right[len(nums) - 1] = 1

        for i in reversed(range(len(nums) - 1)):
            right[i] = right[i + 1] * nums[i + 1]
        
        for i, _ in enumerate(nums):
            solution[i] = left[i] * right[i]
        
        return solution

        