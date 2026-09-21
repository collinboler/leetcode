class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        letters = []        
        for c in s:
            if c.isalpha() or c.isdigit():
                letters.append(c.lower())

        if len(letters) % 2 == 0:
            right = len(letters) - 1
            for left in range(len(letters) / 2):
                if letters[right] != letters[left]:
                    return False
                right -= 1
            return True
        
        else:
            right = len(letters) - 1
            for left in range(len(letters) // 2):
                if letters[right] != letters[left]:
                    return False
                right -= 1
            return True
