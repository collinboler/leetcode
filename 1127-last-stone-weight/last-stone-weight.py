import heapq
class Solution: 
    def lastStoneWeight(self, stones: list[int]) -> int:
        for i in range(len(stones)):
            stones[i] *= -1
        heapq.heapify(stones)

        while len(stones) > 1:
            max1 = heapq.heappop(stones)
            max2 = heapq.heappop(stones)
            if max1 != max2:
                heapq.heappush(stones, max1 - max2)
        
        return -heapq.heappop(stones) if stones else 0
            



        
        