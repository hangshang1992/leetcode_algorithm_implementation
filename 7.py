class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        r = cmp(x,0)
        s = int(str(r*x)[::-1])
        return s*r*(s<2**31)
