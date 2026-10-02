class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n = len(nums) - 1
        if n == 0:
            return nums[0]

        left, right = 0, n
        if nums[right] > nums[left]:
            return nums[left]
 
        # find jump
        while left <= right:
            # mid = (left + right) // 2# make sure doesn't overflow
            mid = (left + right) // 2
            if nums[mid + 1] < nums[mid]:
                return nums[mid + 1]
            # if nums[mid - 1] > nums[mid]:
            #     return nums[mid]
            # on left
            if nums[mid] >= nums[0]:
                left = mid + 1
                
            else:
                right = mid - 1
            
            
