class Solution:
    # log(n)
    def findMinMax(self, nums):
        if len(nums) == 1:
            return (0,0)
        left, right = 0, len(nums) - 1
        if nums[right] > nums[left]:
            return (nums[left], nums[right])
        solution = 0

        while left <= right:
            mid = (left + right) // 2
            if nums[mid + 1] < nums[mid]:
                return (mid + 1, max(0, mid - 1))
            if nums[0] <= nums[mid]:
                left = mid + 1
            else:
                right = mid - 1

    def binarySearch(self, nums, left, right, target):
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid

            if nums[mid] < target:
                left = mid + 1     
            else:
                right = mid - 1
        return -1
    def search(self, nums: list[int], target: int) -> int:
        minI, maxI = self.findMinMax(nums) 
        # then do binary search on the two split arrays
        print("minI: ", minI, "maxI: ", maxI)
        if minI < maxI:
            print("special")
            return self.binarySearch(nums, 0, len(nums) - 1, target)

        if nums[0] <= target:
            print("hi1")
            
            left, right = 0, minI
        else:
            print("hi2")
            left, right = minI, len(nums) - 1
        
        return self.binarySearch(nums, left, right, target)
        








        