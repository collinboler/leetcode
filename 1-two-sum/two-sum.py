class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        map = {}
        for i in range(len(nums)):
            complement = target - nums[i];
            if complement in map:
                return [i, map[complement]]
            else:
                map[nums[i]] = i
        
        return ""
        
        