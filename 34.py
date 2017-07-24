class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums: return [-1, -1]
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            middle = (end - start)/2 + start
            if nums[middle] == target:
                end = middle
            elif nums[middle] < target:
                start = middle
            else:
                end = middle
        if nums[start] == target:
            left = start
        elif nums[end] == target:
            left = end
        else:
            return [-1,-1]
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            middle = (end - start)/2 + start
            if nums[middle] == target:
                start = middle
            elif nums[middle] < target:
                start = middle
            else:
                end = middle
        if nums[end] == target:
            return [left, end]
        else:
            return [left, start]
