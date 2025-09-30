class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        map = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement not in map:
                map[nums[i]] = i
            else:
                return map[complement], i

        return null

        
        