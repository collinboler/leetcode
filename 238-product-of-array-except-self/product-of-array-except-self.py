class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        left, right, result = length * [0], length * [0], length * [0]

        # prefix sum
        # prefix = [nums[0]]
        # for i in range(1, len(nums)):
        #     prefix.append(prefix[i - 1] + nums[i])
        
        # left 
        left[0] = 1

        for i in range(1, length):
            left[i] = (left[i - 1] * nums[i - 1])

        # right
        right[length - 1] = 1

        for i in reversed(range(length - 1)):
            right[i] = (right[i + 1] * nums[i + 1])
        
        for i in range(length):
            result[i] = right[i] * left[i]

        return result
        
        