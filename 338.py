class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        return ['{0:032b}'.format(i).count("1") for i in range(num+1)]
