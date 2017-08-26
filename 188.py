class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        n = len(prices)
        if k >= n / 2:
            return sum(i - j for i, j in zip(prices[1:], prices[:-1]) if i - j > 0)
        res = [[float('-inf') for i in range(2*k + 1 + 1)] for _ in range(n + 1)]
        res[0][1] = 0
        for i in range(1, n + 1):
            for j in range(1, 2*k + 2, 2):
                res[i][j] = res[i-1][j]
                if j > 1 and i >= 2:
                    res[i][j] = max(res[i][j], res[i-1][j-1] + prices[i-1]-prices[i-2])
            for j in range(2, 2*k+2, 2):
                res[i][j] = res[i-1][j-1]
                if j >= 2:
                    res[i][j] = max(res[i][j], res[i-1][j] + prices[i-1]-prices[i-2])
        return max(res[n])
