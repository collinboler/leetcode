class Solution(object):
    def getKey(self, string):
        return "".join(sorted(string))

    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagrams = {}
        for string in strs:
            key = self.getKey(string)
            if key in anagrams:
                anagrams[key].append(string)
            else:
                anagrams[key] = [string]
        solution = []
        for val in anagrams.values():
            solution.append(val)
        
        return solution






        