class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        if len(nums) == 1: return nums[0]
        low_value = high_value = low_value1 = high_value1 = 0
        for item in nums[:-1]:
            low_value, high_value = high_value, max(high_value, low_value + item)
        for item in nums[1:]:
            low_value1, high_value1 = high_value1, max(high_value1, low_value1 + item)
        return max(high_value, high_value1)
