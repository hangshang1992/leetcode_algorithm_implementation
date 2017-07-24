class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            middle = (end - start)/2 + start
            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                end = middle
            else:
                start = middle
        if nums[start] == target:
            return start
        elif nums[end] == target:
            return end
        elif nums[start] > target:
            return start
        elif nums[end] < target:
            return end + 1
        else:
            return end
