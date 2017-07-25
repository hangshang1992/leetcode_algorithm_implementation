class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        right = len(nums) - 1
        if len(nums) <= 1: 
            nums[:] = nums
        else:
            while right > 0 and nums[right] <= nums[right - 1]:
                right -= 1
            if right == 0:
                return self.reverse(nums, 0, len(nums) - 1)
            right -= 1
            left = 0
            for i in range(len(nums)-1, right, -1):
                if nums[i] > nums[right]:
                    left = i
                    break
            nums[right], nums[left] = nums[left], nums[right]
            self.reverse(nums, right + 1, len(nums) - 1)
    def reverse(self, nums, l, r):
        while l<r: 
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
