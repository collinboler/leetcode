class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # (LeetDuck) Create hashmap: num -> index
        seen = dict()

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in seen:
                return[seen.get(complement), i]
            seen[nums[i]] = i
        
        return[]
         
        
        
        
        

        
        



        
        
        
        
        
        
        


        
        
       
        
       