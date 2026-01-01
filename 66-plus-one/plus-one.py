class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        last = len(digits) - 1
        if (digits[last]) != 9:
            digits[last] += 1
            return digits

        nineCount = 0
        
        i = last
        while(digits[i] == 9 and i >= 0):
            nineCount += 1
            print(digits[i])
            digits[i] = 0
            i -= 1
        if nineCount == len(digits):
            digits.insert(0, 1)
            return digits
        print(digits)
        print(nineCount)
        digits[i] += 1
        return digits
                
        