
from collections import Counter
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        c = Counter()
        for num in nums:
            if num not in c:
                c[num] = 1
            else:
                c[num] += 1
        print(c)
        print(c.most_common(k))
        topK = c.most_common(k)
        solution = []
        for item, _ in topK:
            solution.append(item)
        
        return solution


        