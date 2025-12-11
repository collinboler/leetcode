class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        m = {}
        for i in range(len(s)):
            if s[i] not in m:
                m[s[i]] = 1
            else:
                m[s[i]] = m.get(s[i]) + 1
        
        for j in range(len(t)):
            if t[j] not in m:
                return False
            elif m.get(t[j]) > 1:
                m[t[j]] = m.get(t[j]) - 1
            else:
                del m[t[j]]
        
        return True



        