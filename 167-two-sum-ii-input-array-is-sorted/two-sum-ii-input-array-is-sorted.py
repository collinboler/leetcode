class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # for num in reversed(numbers):
        #     if num > target:
        #         numbers.pop()
        
        left, right = 0, len(numbers) - 1

        while (left < right):
            twoSum = numbers[left] + numbers[right]
            if twoSum == target:
                return [left + 1, right + 1]
            elif twoSum > target:
                right -= 1
            else:
                left += 1
        
        return []

        