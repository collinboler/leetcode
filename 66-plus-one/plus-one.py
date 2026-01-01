class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # last = len(digits) - 1
        # if digits[last] != 9:
        #     digits[last] += 1
        #     return digits
        # else: # last digit is 9

        #     digits[last] = 1
        #     digits.append(0)
        #     i = last - 1 
        #     while (digits[i] == 9):
        #         digits[i + 1] = 0
        #         digits[i] = 1
        #         i -= 1
        #     digits[i + 1] += 1
        stringy = ""
        for digit in digits:
            stringy += str(digit)

        result = int(stringy) + 1

        resultString = str(result)

        resultList = []
        for ch in resultString:
            resultList.append(int(ch))
        return resultList

        