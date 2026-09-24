class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = []

        pairs = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }

        for c in s:
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
            elif not stack:
                return False
            elif stack[-1] != pairs[c]:
                return False
            else:
                stack.pop()
        
        return not stack

        