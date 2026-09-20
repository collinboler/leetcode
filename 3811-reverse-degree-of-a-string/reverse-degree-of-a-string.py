def getScore(i, c):
    # (LeetDuck) Review how this helper is scoped and referenced inside the class.
    reverseOrder = 26 - (ord(c) - 97)
    return reverseOrder * (i + 1)

class Solution(object):
    
    
    def reverseDegree(self, s):
        """
        :type s: str
        :rtype: int
        """
        solution = 0
        for i, c in enumerate(s):
            solution = solution + getScore(i, c)
        return solution
        