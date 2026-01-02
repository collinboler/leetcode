import heapq
class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        if len(sticks) < 1:
            return 0
        heap = []
        heapq.heapify(heap)
        for stick in sticks:
            heapq.heappush(heap, stick)
        work = 0
        while (len(heap) >= 2):
            stick1 = heapq.heappop(heap)
            stick2 = heapq.heappop(heap)

            work += stick1 + stick2
            if len(heap) != 0:
                heapq.heappush(heap, stick1 + stick2)


        return work


        