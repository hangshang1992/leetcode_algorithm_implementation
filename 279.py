class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = [float('inf')] * (n+1)
        res[0] = 0
        for i in range(1, n + 1):
            for j in range(int(math.sqrt(i)) + 1):
                res[i] = min(res[i], res[i-j**2] + 1)
        return res[-1]
