class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums)<=1:
            nums[:] = nums
        else:
            left = len(nums) - 1
            while left > 0 and nums[left] <=  nums[left - 1]:
                left -= 1
            if left == 0:
                return self.reverse(nums, 0, len(nums) - 1)
            left -= 1
            right = 0
            for i in range(len(nums)-1, left, -1):
                if nums[i] > nums[left]:
                    right = i
                    break
            nums[left], nums[right] = nums[right], nums[left]
            self.reverse(nums, left + 1, len(nums)-1)
    def reverse(self, nums, l, r):
        while l<r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
