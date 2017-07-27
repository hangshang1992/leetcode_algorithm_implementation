class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        history_max, current = nums[0], nums[0]
        for item in nums[1:]:
            current = max(item, item+current)
            history_max = max(history_max, current)
        return history_max
