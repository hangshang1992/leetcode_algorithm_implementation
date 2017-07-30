class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start, end = 0, len(nums) - 1
        target = nums[-1]
        while start + 1 < end:
            middle = (end - start)/2 + start
            if nums[middle] <= target:
                end = middle
            else:
                start = middle
        if nums[start] <= target:
            return nums[start]
        else:
            return nums[end]
