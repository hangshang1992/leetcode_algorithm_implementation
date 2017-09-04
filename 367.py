class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        start, end = 0, num
        while start + 1 < end:
            mid = (end - start)/2 + start
            if mid ** 2 == num:
                return True
            if mid**2 > num:
                end = mid
            else:
                start = mid
        if start ** 2 == num or end ** 2 == num:
            return True
        else:
            return False
