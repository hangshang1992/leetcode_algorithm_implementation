class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        if num == 0:
            return [0]
        res = [0] * (num + 1)
        res[1] = 1
        for i in range(2, num + 1):
            res[i] = res[i>>1] + i%2
        return res
