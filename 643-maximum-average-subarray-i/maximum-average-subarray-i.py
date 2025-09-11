class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        left = 0
        curr = 0
        answer = float('-inf')

        for right in range(len(nums)):
            curr += nums[right]
            while (right - left) >= k:
                
                curr -= nums[left]
                left += 1
            if (right - left + 1) == k:
                answer = max(answer, curr)
        
        return float(answer) / float(k)