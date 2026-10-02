class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        n = len(temperatures)
        stack = []
        result = [0] * n
        for i, temp in enumerate(temperatures):
            if stack:
                while stack and stack[-1][0] < temp:
                    _, index = stack.pop()
                    result[index] = i - index
            stack.append((temp, i))
            # store temp and i val
        return result
