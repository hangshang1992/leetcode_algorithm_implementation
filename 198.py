class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        if len(nums) == 1: return nums[0]
        current_value, max_value = nums[0], max(nums[0], nums[1])
        for i in range(2,len(nums)):
            max_value, current_value = max(max_value, current_value + nums[i]) ,max_value
        return max_value
