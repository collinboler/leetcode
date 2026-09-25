import heapq
class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        length = len(temperatures) - 1
        heap = []
        solution = []
        for i, temp in enumerate(temperatures):
            if heap:
                
                while temp > heap[0][0]: # temp >
                    # print("-temp: %s, -heapVal: %s" % (temp, heap[0][0]))
                    # print("solution now was %s and now is %s" % (solution[heap[0][1]], i - heap[0][1]))
                    solution[heap[0][1]] = i - heap[0][1]
                    heapq.heappop(heap)
                    if not heap:
                        break
            heapq.heappush(heap, (temp, i))
            solution.append(0)
        return solution
            
            
