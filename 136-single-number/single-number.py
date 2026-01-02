class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashlist = []

        for num in nums:
            if num not in hashlist:
                hashlist.append(num)
            else:
                hashlist.remove(num)
        
        return hashlist.pop()

        