class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        b1 = float("-inf")
        b2 = float("-inf")
        s1 = 0
        s2 = 0
        for i in range(len(prices)):
            b1 = max(b1, -prices[i])
            s1 = max(s1, prices[i] + b1)
            b2 = max(b2, s1 - prices[i])
            s2 = max(s2, b2 + prices[i])
        return s2
