class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(nums) < 2:
            return False
        for i in range(len(nums)):
            sum1 = nums[i]
            for j in range(i + 1, len(nums)):
                sum1 += nums[j]
                if k == 0 and sum1 == k:
                    return True
                if k != 0 and sum1 % k == 0:
                    return True
        return False
               
