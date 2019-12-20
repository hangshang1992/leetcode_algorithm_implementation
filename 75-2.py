class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        self.quicksort(nums, 0, len(nums) - 1)
    
    def quicksort(self, nums, start, end):
        if start >= end:
            return
        low, high = start, end
        base = nums[start]
        while low < high:
            while low < high and nums[high] >= base:
                high -= 1
            nums[low] = nums[high]
            while low < high and nums[low] <= base:
                low += 1
            nums[high] = nums[low]
        nums[low] = base
        self.quicksort(nums, start, low - 1)
        self.quicksort(nums, low + 1, end)
