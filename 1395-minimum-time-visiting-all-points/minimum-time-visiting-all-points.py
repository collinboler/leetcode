class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        # (LeetDuck) Time = sum of max(|dx|, |dy|) for consecutive points
        
        time = 0

        for i in range(len(points) - 1):
            
            point = points[i]
            point2 = points[i+1]

            time += max(abs(point[0] - point2[0]), abs(point[1] - point2[1]))


            # if points[i+2] == null:
            #     break
        
        return time
        

            
            

            


        