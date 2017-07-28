class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        res = [float('inf') for _ in range(amount+1)]
        res[0] = 0
        for n in coins:
            for i in range(amount+1):        
                if i>=n:
                    res[i] = min(res[i], res[i-n] + 1)
        if res[-1] == float('inf'):
            return -1
        return res[-1]
