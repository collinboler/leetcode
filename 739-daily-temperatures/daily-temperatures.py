class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stack = []
        result = []
        for i, temp in enumerate(temperatures):
            if stack:
                while stack and stack[-1][0] < temp:
                    _, index = stack.pop()
                    result[index] = i - index
            result.append(0)
            stack.append((temp, i))
            # store temp and i val
        return result
