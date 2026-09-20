class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # lengths unequal
        if len(s) != len(t):
            return False

        # store chars in first string
        sMap = {}
        for char in s:
            if char in sMap:
                sMap[char] = sMap[char] + 1
            else:
                sMap[char] = 1

        # check against second string
        for char in t:
            if char in sMap:
                if (sMap[char] > 1):
                    sMap[char] = sMap[char] - 1
                else:
                    del sMap[char]
            else:
                return False
        
        return True
                


        
       



        