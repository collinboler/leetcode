class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        solution = 0
        n = len(nums)
        for i, num in enumerate(nums):
            if n % (i + 1) == 0:
                solution += num * num
        return solution

        
        