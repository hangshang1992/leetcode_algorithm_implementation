class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        write = 0
        for read in range(length):
            if nums[read]!= 0:
                nums[write] = nums[read]
                write += 1
        while write < length:
            nums[write] = 0
            write += 1
            
