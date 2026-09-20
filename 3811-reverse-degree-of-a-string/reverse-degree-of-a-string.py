class Solution(object):

    def getScore(self, i, c):
        reverseOrder = 26 - (ord(c) - 97)
        return reverseOrder * (i + 1)

    def reverseDegree(self, s):
        """
        :type s: str
        :rtype: int
        """
        solution = 0
        for i, c in enumerate(s):
            solution = solution + self.getScore(i, c)
        return solution
        