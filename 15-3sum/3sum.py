class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        seen = {}
        solution = set()
        sums = set(nums)
        dups = set()

        for i, val1 in enumerate(nums):
            if val1 not in dups:
                dups.add(val1)
            for j in range(i + 1, len(nums)):
                val2 = nums[j]
                complement = -val1 - val2
                if complement in seen and seen[complement] == i:
                    solution.add(tuple(sorted((val1, val2, complement))))
                seen[val2] = i
        return [list(x) for x in solution]