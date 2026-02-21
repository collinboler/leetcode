class Solution(object):

    def isValid(self, num):
        binary = bin(num)[2:]
        ones = 0
        for c in binary:
            if c == '1': 
                ones += 1
        return self.isPrime(ones)
    
    def isPrime(self, num):
        if num <= 1:
            return False
        for i in range(2, int(math.sqrt(num) + 1)):
            if num % i == 0:
                return False
        return True

    def countPrimeSetBits(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        solution = 0
        while left < right + 1:
            print(left)
            print(self.isValid(left))
            if (self.isValid(left)):
                solution += 1
            left += 1
        
        return solution

        