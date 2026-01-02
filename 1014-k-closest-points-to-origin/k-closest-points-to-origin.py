import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        map = {}

        h = []
        for x, y in points:
            dist = x*x + y*y
            heapq.heappush(h, (-dist,x, y))
            if len(h) > k:
                heapq.heappop(h)
        
        result = []
        print(h)
        print(map)

        for _, x, y in h:
            arr = []
            arr.append(x)
            arr.append(y)
            result.append(arr)

        return result
    
    def eDist(self, x: int, y: int) -> int:
        return math.sqrt((x*x) + (y*y))


    