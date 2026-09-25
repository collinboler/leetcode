class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        # length = len(temperatures) - 1
        stack = []
        solution = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]: # temp >
                solution[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)
        return solution
            
            
