import heapq

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        h = []
        heapq.heapify(h)

        for pile in piles:
            heapq.heappush(h, -pile)
        

        result = 0
        for i in range(k):
            val = heapq.heappop(h)
            heapq.heappush(h, math.floor(val / 2))

           
        for x in h:
            result += -x
            
        
        return result


        