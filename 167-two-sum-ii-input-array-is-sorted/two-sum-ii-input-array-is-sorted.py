class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # i = len(numbers) - 1
        # while (numbers[i] > target):
        #     numbers.pop()
        #     i -= 1
        
        left, right = 0, len(numbers) - 1

        while left < right:
            twoSum = numbers[left] + numbers[right]
            if twoSum == target:
                return [left + 1, right + 1]
            elif twoSum < target:
                left += 1
            elif twoSum > target:
                right -= 1
        return []
        