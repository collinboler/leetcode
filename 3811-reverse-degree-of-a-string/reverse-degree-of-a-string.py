class Solution(object):

    def getScore(self, i, c):
        reverseOrder = 26 - (ord(c) - 97)
        return reverseOrder * (i + 1)

    def reverseDegree(self, s):
        """
        :type s: str
        :rtype: int
        """
        # (LeetDuck) Use a qualified reference to the class helper here.
        solution = 0
        for i, c in enumerate(s):
            solution = solution + self.getScore(i, c)
        return solution
        