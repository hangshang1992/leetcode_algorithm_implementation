class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        ans = float("inf")
        j = 0
        sum1 = 0
        for i in range(len(nums)):
            while j < len(nums) and sum1 < s:
                sum1 += nums[j]
                j += 1
            if sum1 >= s:
                ans = min(ans, j-i)
            sum1 -= nums[i]
        if ans == float('inf'):
            return 0
        return ans
        
