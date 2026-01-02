class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        points.sort(key=self.dist)

        return points[:k]

    def dist(self, point):
        return point[0] ** 2 + point[1] ** 2
        