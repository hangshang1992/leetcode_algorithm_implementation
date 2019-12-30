class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        l1 = len(text1) + 1
        l2 = len(text2) + 1
        dp = [[0 for _ in range(l1)] for _ in range(l2)]
        for i in range(l2):
            for j in range(l1):
                if i == 0 or j == 0:
                    dp[i][j] = 0
                elif text1[j-1]==text2[i-1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]
