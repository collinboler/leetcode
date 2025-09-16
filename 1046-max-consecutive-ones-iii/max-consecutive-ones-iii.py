class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        left = 0
        zeros = 0
        best = 0
     
        for right in range(len(nums)):
            if (nums[right] == 0):
                zeros += 1
            while (zeros > k):
                
                if (nums[left] == 0):
                    zeros -= 1
                left += 1
            best = max(best, right - left + 1)
           
         
                
        
        
        return best
                
            

             
        