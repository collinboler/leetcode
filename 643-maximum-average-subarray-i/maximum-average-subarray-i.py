class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
       
        curr = sum(nums[:k])
        answer = curr
        for i in range(k, len(nums)):
            curr += nums[i ] - nums[i - k]

            answer = max(answer, curr)
        
        return float(answer) / k 