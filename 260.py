class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        test, test1, a, b = reduce(lambda x,y:x^y, nums), 1, 0, 0
        while test&test1 == 0:
            test1 = test1 << 1
        for item in nums:
            if test1&item == 0:
                a ^= item
            else:
                b ^= item
        return [a,b]
