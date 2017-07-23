class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = [0 for _ in range(n+1)]
        result[0] = 1
        result[1] = 1
        if n<= 1: return result[n]
        for i in range(2, n+1):
            for j in range(i):
                result[i] += result[j] * result[i-j-1]
        return result[n]
