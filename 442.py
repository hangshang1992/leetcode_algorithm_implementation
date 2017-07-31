class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for item in nums:
            if nums[abs(item) - 1] < 0:
                res.append(abs(item))
            else:
                nums[abs(item) - 1] = -1*nums[abs(item) - 1]
        return res
