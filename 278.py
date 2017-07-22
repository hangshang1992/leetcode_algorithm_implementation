# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start, end = 1, n
        while start + 1 < end:
            middle = (end - start)/2 + start
            if isBadVersion(middle):
                end = middle
            else:
                start = middle
        if isBadVersion(start):
            return start
        else:
            return end
