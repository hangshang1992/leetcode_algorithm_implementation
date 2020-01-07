class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return self.quickSort(nums, 0, len(nums) - 1, len(nums) - k)

    
    def quickSort(self, nums, start, end, k):

        l, r = start, end
        base = nums[start]
        while l < r:
            while l < r and nums[r] >= base:
                r -= 1
            nums[l] = nums[r]
            while l < r and nums[l] <= base:
                l += 1
            nums[r] = nums[l]
        nums[l] = base
        if l == k:
            return nums[l]
        elif l > k:
            return self.quickSort(nums, start, l - 1, k)
        else:
            return self.quickSort(nums, l + 1, end, k)
