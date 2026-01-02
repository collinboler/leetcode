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
            # result += math.floor(val / 2)
            heapq.heappush(h, math.floor(val / 2))

            # print(f"iteration  {i + 1} out of {k}; result = {result}, val = {val}")
        
        # print(h)
        for x in h:
            result += -x
            
        
        return result


        