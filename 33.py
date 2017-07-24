class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums: return -1
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            middle = (end - start)/2 + start
            if nums[middle] == target:
                return middle
            if nums[middle] > nums[start]:
                if nums[middle] >= target and nums[start] <= target:
                    end = middle
                else:
                    start = middle
            else:
                if nums[middle] <= target and nums[end] >= target:
                    start = middle
                else:
                    end = middle
        print start, end
        if nums[start] == target:
            return start
        elif nums[end] == target:
            return end
        else:
            return -1
        
