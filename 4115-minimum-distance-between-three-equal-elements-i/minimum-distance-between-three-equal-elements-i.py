class Solution(object):
    def minimumDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        positions = defaultdict(list)

        for i, x in enumerate(nums):
            positions[x].append(i)

        best = float('inf')

        for idxs in positions.values():
            if len(idxs) >= 3:
                for i in range(len(idxs) - 2):
                    best = min(best, 2 * (idxs[i + 2] - idxs[i]))

        return -1 if best == float('inf') else best
        
        