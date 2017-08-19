class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        if len(nums)<=k:
            return sum(nums)*1.0/len(nums)
        temp = sum(nums[:k-1])
        res = float("-inf")
        for i in range(k-1, len(nums)):
            temp += nums[i]
            res = max(res, temp)
            temp -= nums[i-k+1]
        return res*1.0/k
