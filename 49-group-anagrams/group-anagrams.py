class Solution(object):

    def sortStr(self, string):
        return ''.join(sorted(string))

    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hashmap = {} # of string and stacks
        for string in strs:
            sortd = self.sortStr(string)
            if sortd not in hashmap:
                set = []
                set.append(string)
                hashmap[sortd] = set
            else:
                hashmap[sortd].append(string)
        
        result = []
        for _, value in hashmap.items():
            result.append(value)
        
        return result




            


        