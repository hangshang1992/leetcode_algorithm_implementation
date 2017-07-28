class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        dp = [0 for _ in range(amount + 1)]
        dp[0] = 1 
        for i in range(len(coins)):
            for j in range(amount + 1):
                new_amount = j + coins[i]
                if new_amount > amount or dp[j] == 0: continue
                dp[new_amount] += dp[j]
        return dp[amount]
