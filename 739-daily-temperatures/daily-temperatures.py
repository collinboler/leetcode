import heapq
class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        # length = len(temperatures) - 1
        stack = []
        solution = []
        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]: # temp >
                solution[stack[-1][1]] = i - stack[-1][1]
                stack.pop()
                if not stack:
                    break
            stack.append((temp, i))
            solution.append(0)
        return solution
            
            
