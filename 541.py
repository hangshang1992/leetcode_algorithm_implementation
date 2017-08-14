class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        nums = list(s)
        for i in range(0, len(nums), 2*k):
            nums[i:i+k] = reversed(nums[i:i+k])
        return ''.join(nums)
