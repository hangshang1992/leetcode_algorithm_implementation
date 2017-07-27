class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = dict()
        for item in nums:
            dic[item] = 0
        write = 0
        for i in range(len(nums)):
            if dic[nums[i]] < 2:
                nums[write] = nums[i]
                dic[nums[i]] += 1
                write += 1
        return write
