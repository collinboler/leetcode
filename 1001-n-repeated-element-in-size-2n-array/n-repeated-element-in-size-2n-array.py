class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        # simple one pass solution
        maxNum = -1
        maxy = 0
        mappy = {}

        for num in nums:
            if num in mappy:
                mappy[num] += 1
                if (mappy[num] > maxy):
                    maxNum = num
                    maxy = mappy[num]
            else: 
                mappy[num] = 1
        
        return maxNum
            
                   
            
            



        



        
        