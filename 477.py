class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        mask = 1
        for i in range(32):
            ones = zeros = 0
            for num in nums:
                if num&mask == 0:
                    zeros+= 1
                else:
                    ones += 1
            ans += ones * zeros
            mask = mask << 1
        return ans
