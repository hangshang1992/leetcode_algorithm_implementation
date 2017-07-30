class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = nums[0]
        for item in nums[1:]:
            res = min(res,item)
        return res
