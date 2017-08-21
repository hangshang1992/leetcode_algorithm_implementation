class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n <= 1:
            return 0
        res = [float('inf')] * (n + 1)
        res[0] = 0
        isPalind = self.isPalin(s)
        for i in range(1, n+1):
            for j in range(i):
                if isPalind[j][i-1]:
                    res[i] = min(res[i], res[j] + 1)
        return res[-1] - 1
    def isPalin(self, s):
        n = len(s)
        res = [[False for _ in range(n)] for _ in range(n)]
        # odd
        for mid in range(n):
            i = j = mid
            while i >= 0 and j < n and s[i] == s[j]:
                res[i][j] = True
                i -= 1
                j += 1
        for mid in range(n-1):
            i = mid
            j = mid + 1
            while i >= 0 and j < n and s[i] == s[j]:
                res[i][j] = True
                i -= 1
                j += 1
        return res
