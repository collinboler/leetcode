class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        bigList = []
        for i in range(numRows): 
            if (i == 0):
                bigList.append([1]) 
            elif (i == 1):
                bigList.append([1,1])     
            else:
                prev = bigList[-1]
                row = [1]
                for j in range(1, len(prev)):
                    row.append(prev[j - 1] + prev[j])
                row.append(1)
                bigList.append(row)
        return bigList
                 
           
        
        
            

       
        