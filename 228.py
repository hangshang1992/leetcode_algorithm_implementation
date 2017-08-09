class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        def getRange(begin, end):
            return str(begin)+"->" + str(end) if begin != end else str(begin)
        n = len(nums)
        if n==0:
            return []
        res = []
        pre = start = nums[0]
        for num in nums:
            cur = num 
            if cur - pre > 1:
                res.append(getRange(start, pre))
                start = cur
            if cur == nums[-1]:
                res.append(getRange(start, cur))
            pre = cur
        return res
