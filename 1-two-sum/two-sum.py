class Solution(object):
    def twoSum(self, nums, target):
        """
        # (LeetDuck) Please add your implementation logic here.
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        prev_map = {}  # val : index
    
        for i, n in enumerate(nums):
            diff = target - n
            # If the required complement is already in our map, return the pair
            if diff in prev_map:
                return [prev_map[diff], i]
            # Otherwise, add current number and its index to the map
            prev_map[n] = i
        return []
       
       
       


        
       
        
      
