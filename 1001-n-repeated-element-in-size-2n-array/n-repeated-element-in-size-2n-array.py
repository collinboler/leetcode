class Solution(object):
    def repeatedNTimes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        setty = set()

        for num in nums:
            if num in setty:
                return num
            
            else:
                setty.add(num)
        
        return -1
        