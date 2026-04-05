class Solution:
    def judgeCircle(self, moves: str) -> bool:
        L = 0
        R = 0
        U = 0
        D = 0

        for move in moves:
            if move == 'U':
                U += 1
            elif move == 'D':
                D += 1
            elif move == 'R':
                R += 1
            elif move == 'L':
                L += 1
        
        if L != R or U != D:
            return False
        return True
        
        