class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            middle = (end - start)/2 + start
            if nums[middle] > nums[middle-1] and nums[middle] >nums[middle+1]:
                return middle
            elif nums[middle] < nums[middle-1] and nums[middle] < nums[middle+1]:
                end = middle
            elif nums[middle] < nums[middle - 1] and nums[middle] > nums[middle+1]:
                end = middle
            else:
                start = middle
        if nums[start] > nums[end]:
            return start
        else:
            return end
