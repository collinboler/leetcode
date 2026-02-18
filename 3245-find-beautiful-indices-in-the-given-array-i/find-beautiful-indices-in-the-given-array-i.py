class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        A = []
        B = []
        n = len(s)
        la = len(a)
        lb = len(b)

        # 1) Collect occurences of a and b
        i = 0 # sort A list
        while i <= n-la:
            if(s[i:i+la] == a):
                A.append(i)
            i+=1
        
        j = 0 # sort B list
        while j <= n-lb:
            if(s[j:j+lb] == b):
                B.append(j)
            j+=1

        # 2) TWO POINTER SWEEP
        
        p = 0 # pointer
        m = len(B)
        ans = []

        # abs(j-i)<= k
        for i in A:
            L = i - k # left boundary
            R = i + k # right boundary
        
            # discard b occurences that are too far
            # left to work for >= i
            while p < m and B[p] < L: 
                p += 1

            # check if p within L range are also
            # within R range
            if p < m and B[p] <= R:
                ans.append(i)

        return ans
                


        