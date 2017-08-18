class Solution(object):
    def maxDistance(self, arrays):
        """
        :type arrays: List[List[int]]
        :rtype: int
        """
        res, currMax, currMin = 0, float("-inf"), float("inf")
        for a in arrays:
            res = max(res, max(currMax - a[0], a[-1] - currMin))
            currMax, currMin = max(currMax, a[-1]), min(currMin, a[0])
        return res
