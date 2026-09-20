class Solution(object):
    def whichGrid(self, row, col):
        if row <= 2:
            if col <= 2:
                return 0
            elif col <= 5:
                return 1
            else:
                return 2
        if row <= 5:
            if col <= 2:
                return 3
            elif col <= 5:
                return 4
            else:
                return 5
        else:
            if col <= 2:
                return 6
            elif col <= 5:
                return 7
            else:
                return 8
        return 0
    
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        columns = {}
        i = 0
        while i < 9:
            columns[i] = set()
            i += 1

        grids = {}
        i = 0
        while i < 9:
            grids[i] = set()
            i += 1
        
        # go through rows
        for rowIndex, rowVal in enumerate(board):
            rowSeen = set()
            # go through col in row x
            for columnIndex, columnVal in enumerate(rowVal):
                if columnVal == ".":
                    continue
            # column check
                elif columnVal in columns[columnIndex]:
                    return False
                columns[columnIndex].add(columnVal)

                # grid check
                gridIndex = self.whichGrid(rowIndex, columnIndex)
                if columnVal in grids[gridIndex]:

                    return False
                grids[gridIndex].add(columnVal)

                # row check
                if columnVal in rowSeen:
                    return False
                else:
                    rowSeen.add(columnVal)
        return True
                
                    
            



        