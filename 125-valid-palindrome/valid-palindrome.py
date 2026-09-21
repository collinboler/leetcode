class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        # remove invalid characters        
        left, right = 0, len(s) - 1

        while left < right:
            print("left: %s, right: %s" % (left,right))
            print("left: %s, right: %s" % (s[left],s[right]))

            if not s[left].isalnum():
                left += 1
                continue
            if not s[right].isalnum():
                right -= 1
                continue
            
            if s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right -= 1
        return True

        
        