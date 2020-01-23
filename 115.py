class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        res = [[0 for _ in range(len(s) + 1)] for _ in range(len(t) + 1)]
        for i in range(len(s) + 1):
            res[0][i] = 1
        for i in range(1, len(t) + 1):
            for j in range(1, len(s) + 1):
                res[i][j] = res[i][j - 1]
                if t[i-1] == s[j-1]:
                    res[i][j] += res[i-1][j-1]
        return res[-1][-1]
