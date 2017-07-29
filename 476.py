class Solution(object):
    def findComplement(self, n):
        """
        :type num: int
        :rtype: int
        """
        return int(len(bin(n)[2:]) * '1',2)^n
