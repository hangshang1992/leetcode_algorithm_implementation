class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        start, end = 1, x
        while start + 1 < end:
            mid = (end-start)/2 + start
            if mid**2 <= x:
                start = mid
            else:
                end = mid
        if start ** 2 <= x:
            return start
        return end
