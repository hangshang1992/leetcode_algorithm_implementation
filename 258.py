class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        a = str(num)
        while len(a) > 1:
            a = str(sum([int(item) for item in a]))
        return int(a)
